# nafuda

builderscon の nafuda に自分の作ったプログラムを載せたかった。

## 使ってるライブラリ

epdの[demo code](https://www.waveshare.com/wiki/File:4.2inch_e-paper_module_code.7z)にPython 3用に使えるようにしたものを再配布

# INSTALL

フォント(SymbolaとVLゴシック)

	$ sudo apt-get install ttf-ancient-fonts
	$ sudo apt-get install fonts-vlgothic

Python 3.5 venvが遅いかも

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

Systemdに変更あったらdaemon-reload

	$ sudo systemctl daemon-reload

Systemdへ起動時にフックさせる

	$ sudo systemctl enable paper.service 
