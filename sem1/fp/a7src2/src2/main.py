from repository import MemoryRepository
from repository import TextFileRepository
from repository import BinaryFileRepository
from repository import JsonFileRepository
from services import Services
from ui import Ui
from tests import Tests

tests = Tests()
#tests.test_all()

mem_repo = MemoryRepository()
text_repo = TextFileRepository()
bin_repo = BinaryFileRepository()
json_repo = JsonFileRepository()

serv = Services(json_repo)
ui = Ui(serv)
ui.start_loop()

