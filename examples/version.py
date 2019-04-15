import ztools

# 显示 Timeout 版本号
ztools_timeout = ztools.Timeout()
ztools_timeout.Version(isShow = True)

# 显示 ProgressBar 版本号
ztools_progressbar = ztools.ProgressBar()
ztools_progressbar.Version(isShow = True)

# 显示 Plot 版本号
ztools_plot = ztools.Plot("test")
ztools_plot.Version(isShow = True)

# 显示 File 版本号
ztools_file = ztools.File()
ztools_file.Version(isShow = True)

# 显示 Xls 版本号
ztools_xls = ztools.Xls()
ztools_xls.Version(isShow = True)

# 显示 MySQL 版本号
ztools_mysql = ztools.MySQL()
ztools_mysql.Version(isShow = True)

input()
