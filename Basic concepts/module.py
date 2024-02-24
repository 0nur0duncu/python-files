import sys
#print(sys.version) #3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]
#import sys as new_name
#print(new_name.version) #3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]

from sys import version,path
print(path) #['c:\\Users\\90539\\Desktop\\python', 'C:\\Users\\90539\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\90539\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\90539\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\90539\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\90539\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']
print(dir(sys))
"""
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_vpath', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']"""
print(help('modules'))
"""
PIL                 _tracemalloc        getpass             re
__future__          _typing             gettext             reprlib
__hello__           _uuid               glob                rlcompleter
__phello__          _warnings           graphlib            runpy
_abc                _weakref            gzip                sched
_aix_support        _weakrefset         hashlib             scipy
_ast                _winapi             heapq               screed
_asyncio            _xxsubinterpreters  hmac                secrets
_bisect             _zoneinfo           html                select
_blake2             abc                 http                selectors
_bootsubprocess     aifc                idlelib             setuptools
_bz2                antigravity         imaplib             shelve
_codecs             argparse            imghdr              shlex
_codecs_cn          array               imp                 shutil
_codecs_hk          ast                 importlib           signal
_codecs_iso2022     asynchat            inspect             site
_codecs_jp          asyncio             io                  six
_codecs_kr          asyncore            ipaddress           smtpd
_codecs_tw          atexit              itertools           smtplib
_collections        audioop             json                sndhdr
_collections_abc    base64              keyword             socket
_compat_pickle      bdb                 kiwisolver          socketserver
_compression        bigtests            lib2to3             sqlite3
_contextvars        binascii            linecache           sre_compile
_csv                bisect              locale              sre_constants
_ctypes             builtins            logging             sre_parse
_ctypes_test        bz2                 lzma                ssl
_datetime           bz2file             mailbox             stat
_decimal            cProfile            mailcap             statistics
_distutils_hack     calendar            marshal             string
_elementtree        cgi                 math                stringprep
_functools          cgitb               matplotlib          struct
_hashlib            chunk               mclahe              subprocess
_heapq              click               mimetypes           sunau
_imp                cmath               mmap                symtable
_io                 cmd                 module              sys
_json               code                modulefinder        sysconfig
_locale             codecs              msilib              tabnanny
_lsprof             codeop              msvcrt              tarfile
_lzma               collections         multiprocessing     telnetlib
_markupbase         colorama            netrc               tempfile
_md5                colorsys            nntplib             test
_msi                compileall          nt                  textwrap
_multibytecodec     concurrent          ntpath              this
_multiprocessing    configparser        nturl2path          threading
_opcode             contextlib          numbers             time
_operator           contextvars         numpy               timeit
_osx_support        contourpy           opcode              tkinter
_overlapped         copy                ope                 token
_pickle             copyreg             operator            tokenize
_py_abc             crypt               optparse            tomllib
_pydecimal          csv                 os                  trace
_pyio               ctypes              packaging           traceback
_queue              curses              pandas              tracemalloc
_random             cv2                 pathlib             tty
_sha1               cycler              pdb                 turtle
_sha256             dataclasses         pickle              turtledemo
_sha3               datetime            pickletools         types
_sha512             dateutil            pip                 typing
_signal             dbm                 pipes               unicodedata
_sitebuiltins       decimal             pkg_resources       unittest
_socket             difflib             pkgutil             urllib
_sqlite3            dis                 platform            uu
_sre                distutils           plistlib            uuid
_ssl                doctest             poplib              venv
_stat               email               posixpath           warnings
_statistics         encodings           pprint              wave
_string             ensurepip           profile             weakref
_threading_local    gc                  queue               zipimport
_tkinter            genericpath         quopri              zlib
_tokenize           getopt              random              zoneinfo"""