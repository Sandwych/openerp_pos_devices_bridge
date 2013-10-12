from bottle import route, run, request, response

def jsonp(dictionary):
    if (request.query.jsonp):
        response.content_type = "application/json"
        return "%s(%s)" % (request.query.jsonp, dictionary)
    return dictionary

def jsonrpcp(result):
    return jsonp(dict(result=result))

@route('/pos/weighting_start')
def weighting_start():
    print "weighting_start"
    return 

@route("/pos/weighting_end")
def weighting_end():
    print "weighting_end"
    return 

@route('/pos/weighting_read_kg')
def weighting_read_kg():
    return jsonrpcp(10.0)

#@app.route("/pos/weighting_read_kg")
#def weighting_read_kg():
#    return jsonify({'result': 10.0})
#@app.route("/pos/print_receipt")
@route('/pos/print_receipt')
def print_receipt():
    print "-----------------"
    print "-----------------"
    try:
        d = request.args.to_dict()[u'r']
    except Error as e:
        print e




if __name__ == "__main__":
    run(host='localhost', port=8069)
