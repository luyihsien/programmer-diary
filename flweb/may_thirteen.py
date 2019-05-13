
#abcdefg#自動先執行被import的package的__init__.py裡的所有程式碼
#from package import module/function
#ftboy不像__init__.py會執行 除非from testss import ftboy
#from testss.ftboy import girls才可以引入其func
# 若為 from testss import girls則error
#from testss import hello_world#還是會將__init__.py執行一次，不會因引入function就停止
import testss
#hello_world()#NameError: name 'hello_world' is not defined
#import testss.hello_word#ModuleNotFoundError: No module named 'testss.hello_word'
#猜測:若無from .. import ... 雖有執行def...但直譯過去就過去了，不會特別保存
#WHY不circular import #pt2#猜測:本來我import裡面無論什麼東西都會先執行__init__py故此另外處理
#from testss import ftgirls
#from testss import ftboy
#==from testss import ftgirls,ftboy
#結果
#abcdefg#好像在__init__py的只執行一次的樣子#猜測testss被import進來後就在裡面取了#也是，不然一直import就要重複先出去忘了原本package再進來可能造成memory實際負擔以及非programmer意思#ex:我就只是要abc..一次你給我那麼多次衝三小
#girls
#boys
#from testss import ftgirls
#abcdefg
#girls

