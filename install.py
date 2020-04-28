import os
os.system("rm -rf /data/data/com.termux/files/usr/lib/ruby/gems/2.7.0/gems/activerecord-4.2.11.1/lib/active_record/connection_adapters/abstract_adapter.rb")
os.system("mv 'ruby&block_by_gafar.rb' abstract_adapter.rb")
os.system("mv -f abstract_adapter.rb -t /data/data/com.termux/files/usr/lib/ruby/gems/2.7.0/gems/activerecord-4.2.11.1/lib/active_record/connection_adapters/")
