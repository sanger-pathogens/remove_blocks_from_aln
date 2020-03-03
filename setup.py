from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys, os, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import subprocess
        errno = subprocess.call([sys.executable, 'tests/runtests.py'])
        raise SystemExit(errno)

setup(
    name = "remove_blocks_from_aln",
    version = "0.1",
    author = "Carla Cummins",
    author_email = "cc21@sanger.ac.uk",
    long_description = read("README.md"),
    license = "GPLv3",
    url = "https://github.com/sanger-pathogens/remove_blocks_from_aln",
    scripts = glob.glob('scripts/*'),
    packages = find_packages(),
    cmdclass = {'test': PyTest}
)
