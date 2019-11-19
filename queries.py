import rdflib

g=rdflib.Graph()
g.parse("G:\论文\设备知识图谱构建\代码\使用owl构建\device_onto5.nt", format="nt")
q='SELECT ?p ?qWHERE{<http://Device.org/onto.owl#DTU15> ?p ?q}'
x=g.query(q)
print(list(x))