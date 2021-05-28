import random as r

countries=['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda',
           'Argentina','Armenia','Australia','Austria','Azerbaijan','Baden',
           'Bahamas','Bahrain','Bangladesh','Barbados','Bavaria','Belarus','Belgium','Belize',
           'Benin','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burma','Burundi',
           'Cambodia','Cameroon','Canada','Chad','Chile','China','Colombia','Comoros','Congo Free State','Costa Rica',
           'Cote d Ivoire','Croatia','Cuba','Cyprus','Czechoslovakia','Egypt','El Salvador',
           'Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Germany','Ghana',
           'Greece','Grenada','Guatemala','Guinea','Guyana','Haiti','Hawaii','Honduras','Hungary','Iceland','India',
           'Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Yugoslavia',
           'Kiribati','Korea','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Lew Chew','Liberia',
           'Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta',
           'Marshall Islands','Mauritius','Mexico','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Namibia',
           'Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway','Oman','Pakistan',
           'Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar',
           'South Korea','Republic of the Congo','Romania','Russia','Rwanda',
           'Samoa','San Marino','Saudi Arabia','Senegal','Serbia','Sierra Leone','Singapore','Slovakia','Slovenia',
           'Solomon Islands','Somalia','South Africa','South Sudan','Spain',
           'Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan',
           'Tanzania','Thailand','Tunisia','Turkey','Turkmenistan','Uganda','Ukraine','United Arab Emirates','United Kingdom',
           'Uruguay','Uzbekistan','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']

body=['eyes','nose','ears','tongue','head','lips','mouth','hairs','teeth','eyebrows','cheeks','chin','neck','shoulder','arm',
      'elbow','palm','wrist','fingers','thumb','skin','chest','stomach','waist','legs','thigh','calf','knee',
      'ankle','foot','back','nails','knee-cap','toes','fist','claw','belly botton']

#-----categories-------
print("choose your category: 1)countries 2)body")
choose=int(input())
if choose==1:
    total_items=len(countries)
    word_number=r.randint(0,total_items)
    word=countries[word_number]
    word=word.lower()
        
elif choose==2:
    total_items=len(body)
    word_number=r.randint(0,total_items)
    word=body[word_number]
    word=word.lower()
else:
    print("invalid choice")



#-----blank for the word to guess , guess is for checking and used is for the letters which have already been used-----#
blank=[]
guess=list(word)
used=[]

#---------for displaying the no of spaces to determine word length-------------
for i in range(0,len(word)):
        if word[i]==' ':
            print(' ',end=' ')
            blank.append(' ')
        else:
            print('_',end=" ")
            blank.append('_')
    

#---i=6 coz no of chances are 6----#
i=6 

#---------main functionality of the game-----------------------
print("\nEnter letters of the word")
    
while i>-1:
    letter=input()
    if len(letter)>1:
        print("not a letter")
        continue
        
    if letter in used:     #--------------- condition for used letters------------------------
        print("You have already used this letter")
        continue
        
    if letter in word:     #-----------------condition is guessed letter is true-------------------------
        used.append(letter)
        for j in range(0,len(word)):
            if letter==word[j]:
                blank[j]=word[j]
        for k in range(0,len(word)):
            print(blank[k],end=" ")
        print("")
        
        if guess==blank:
            print("\n\n!-!-!-!-!-!-!-!-!-!-!-!---YOU WIN---!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("\n!-!-!-!-!-!-!-!-!-!---CONGRATULATIONS---!-!-!-!-!-!-!-!-!-!-!-!-!")
            break
            
    elif i>0:    #-----------------------------------condition if gussed letter is false-----------------------------
        i=i-1
        used.append(letter)
        print(i+1," chances are remaining")
        
        
    elif i==0: #-------------------------condition if all moves are Over
        print("The word was ",word)
        print("\n\nx-x-x-x-x-x-x-x-x-x-x-x---YOU LOSE---x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print("\n-x-x-x-x-x-x-x-x-x-x-GAME OVER-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
        #print("\n\n PLAY AGAIN (y/n)")
        #newgame=input()
        #if newgame.lower==y:
        #    starting()
        #else:
        #    break
