#!/usr/bin/env python3

# Filename: mvc_exceptions.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""File that holds all self-made exceptions."""


class ItemAlreadyStored(Exception):
    pass


class ItemNotStored(Exception):
    pass


class NoResults(Exception):
    pass


class NoPdfFilesFound(Exception):
    pass


class NoDefaultPathSet(Exception):
    pass


class FileDialogError(Exception):
    pass


class ErrorCrawlingFile(Exception):
    pass


if __name__ == "__main__":
    print(__file__)
