import random 
lists = [ 'adam' , 'john', 'ai ']
random_number = random.randint(0,2)
computer_pick3 = lists[random_number]
print("hello my name is " + computer_pick3 )

lists = [ 'nice to meet you' , "it's good to see you ", "what is in your mind"]
random_number = random.randint(0,2)
computer_pick4 = lists[random_number]


lists = [ 'please let me know ' , " I don't like when you're upset", "So what I'm gon' do?"]
random_number = random.randint(0,2)
computer_pick5 = lists[random_number]



lists = [ "If I spoke on your behalf," , "I never cared 'bout what you thought ", "watching Oxygen"]
random_number = random.randint(0,2)
computer_pick6 = lists[random_number]


lists = [ " see you with some other bitch" , "then well, you wouldn't know how to walk", "ex, I could "]
random_number = random.randint(0,2)
computer_pick7 = lists[random_number]


lists = [ "I know that feelin' like it's in my family tree" , "Been on the road ", "Now I know that the medicine be on call"]
random_number = random.randint(0,2)
computer_pick8 = lists[random_number]


list2 = [ computer_pick3 , computer_pick4 , computer_pick5 , computer_pick6 , computer_pick7 , computer_pick8]
random_number = random.randint(0,5)
computer_pick9 = list2[random_number]
print(computer_pick9)
