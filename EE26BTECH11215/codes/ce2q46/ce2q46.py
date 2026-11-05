# ==============================================================================
# Question 46: Zero-Force Member Analysis
# Engineering Rule: If three members meet at a joint where two are collinear 
# (in a straight line) and there is no external load, the third member has zero force.
# ==============================================================================
# Analyze Joint C
# Members AC and CE are collinear, BC is the third member, no external load at C

joint_name1="C", 
member_1="AC", 
member_2="CE", 
third_member="BC", 
has_external_load1=False
collinear1 =True

# Analyze Joint J
# Vertical members are collinear, JK is the third member, no external load at J

joint_name2="J", 
member_1="Lower Column", 
member_2="Upper Column", 
third_member="JK", 
has_external_load2=False
collinear2 = True

if(has_external_load1 == False and collinear1 == True):
    print(f"Joint {joint_name1} has zero force")

if(has_external_load2 == False and collinear2 == True):
    print(f"Joint {joint_name2} has zero force")


