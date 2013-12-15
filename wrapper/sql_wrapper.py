def execute(req):
	print("SELECT {} FROM {} WHERE {}".format(", ".join(req.projection), req.table, req.selection))