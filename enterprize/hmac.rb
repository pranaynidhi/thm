require 'openssl'
sig = OpenSSL::HMAC.hexdigest("SHA1", '712dd4d9c583482940b75514e31400c11bdcbc7374c8e62fff958fcd80e8353490b0fdcf4d0ee25b40cf81f523609c0b', File.read(ARGV[0]))
puts sig
