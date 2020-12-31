def before_all(context):
    context.order_number = '123'
    #import pdb;pdb.set_trace()

def after_all(context):
    context.order_number = 'Bye'
    #import pdb;pdb.set_trace()

# def before_feature(context,feature):
#     context.hello = "beforefeature"
#
#
# def after_feature(context, feature):
#     context.hello = "beforefeature"
#
# def before_scenario(context,scenario):
#     context.hello = "beforefeature"
#
# def before_scenario(context,scenario):
#     context.hello = "beforefeature"
#
# def before_step(context,step):
#     context.hello = "beforefeature"
#
# def after_step(context,step):
#     context.hello  = steps
