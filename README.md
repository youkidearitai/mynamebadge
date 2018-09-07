# nafuda

builderscon の nafuda に自分の作ったプログラムを載せたかった。

## 使ってるライブラリ

epdの[demo code](https://www.waveshare.com/wiki/File:4.2inch_e-paper_module_code.7z)にPython 3用に使えるようにしたもの

# INSTALL

フォント(SymbolaとVLゴシック)

	$ sudo apt-get install ttf-ancient-fonts
	$ sudo apt-get install fonts-vlgothic

Python 3.5

	$ python3.5 -m venv env
	$ . env/bin/activate
	$ pip install -r requirements.txt

## Systemdにセットする

起動時にプログラムが走ってくれると嬉しいので、systemdに登録する。走ってくれると、SDカード入れ替えるだけでe-Paperが書き換わる。

	$ cat /etc/systemd/system/paper.service
	[Unit]
	Description = e-paper init
	After=multi-user.target
	[Service]
	ExecStart=/path/to/dir/paper.sh
	Restart=no
	Type=oneshot
	User=pi
	Group=pi
	[Install]
	WantedBy=multi-user.target
	$ sudo systemctl daemon-reload
	$ sudo systemctl enable paper.service 
