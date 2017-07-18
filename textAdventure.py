def restart():
    ans = input("Replay? ")
    if ans == "Yes":
        replay = True
    elif ans == "No":
        replay = False

replay = True
while replay:
    answer = input("You are escaping from North Korea. Do you attempt to cross over the China-Korea border illegally, fly to China with a fake passport, or attempt to cross over the North-South Korean border? Type 1, 2, or 3. ")
    if answer == "1":
        answer = input("You sneak to the border under the cover of the night, and you realize that you must cross the river to get to China. Do you attempt the crossing? ")
        if answer == "Yes":
            answer = input("You make the dangerous crossing and reach China safely. You make some shady connections and are able to rent an apartment. You hear of a group that wants to sneak out of China to Laos and eventually cross the South China Sea to reach South Korea, which offers shelter to refugees. But you also know that if the Chinese government finds out that your are a refugee, they will send you back to North Korea. Do you attempt to make contact with the group or stay put? Type 1 or 2. ")
            if answer == "1":
                answer = input("You contact the group and it turns out it wasn't a trap. You leave with the group and begin the long travel to Laos. But in order to cross illegally into Laos, you must travel through a forest. Do you want to risk the journey and cross illegaly, or try to cross legally by using a fake identity? Type 1 or 2. ")
                if answer == "1":
                    answer = input("You travel through the jungle, and because you are expecting border patrols, you pack light. Soon into the journey you begin to feel light-headed and tired. You persevere, through, through the jungle, and make it into Laos. But not without cost: you are very sick with an unknown ailment. Do you continue on with the group to Thailand, which offers a safe haven for Korena refugees, or stay back in Laos and try to recover first? Type 1 or 2. ")
                    if answer == "1":
                        print("You make it to Thailand safely. Taiwanese officials help you seek medical help and allow you and the rest of the group to fly to South Korea. Once you reach South Korea, the government offers you all new identities. You live happily in South Korea and have a good life wherein you can listen to Kpop every day :)")
                    elif answer == "2":
                        answer = input("You stay in Laos and attempt to seek medical help, but you have no credentials. Do you attempt to forge an identity to get into the hospital, or attempt to cure yourself? Type 1 or 2. ")
                        if answer == "1":
                            print("Laos officials find out you're a refugee and deport you back to North Korea. You are interrogated for betraying the dear leader and beat mercilessly and sent to work in a labor camp for your betrayal :(")
                        elif answer == "2":
                            print("You succumb to fever and die in Laos. Your body is found later, but nobody arranges your funeral and stuff because you have no friends and no identity since you left North Korea :(")
                elif answer == "2":
                    print("You are spotted and your passport is revealed as fake. The Laos government doesn't have a policy to protect refugees, and sends you back the North Korea. You are interrogated for betraying the dear leader and beat mercilessly and sent a labor camp to work for your betrayal :(")
                elif answer == "2":
                    print("You live the rest of your life in hiding with low-paying jobs. You can't get a better education and better job because you have no identity. If you have children, they will also have no identity and will not be able to go to school. The government doesn't know about you, but your life is pretty bad. You can't seek government help with anything; if you get hurt, you cannot go to a hospital. If you are attacked, you cannot go to the police. Your life sucks, but I guess you're still alive...")
        elif answer == "No":
            print("You decide not to risk it and head back, but guards at the bank see you and capture you. You are interrogated for betraying the dear leader and beat mercilessly :(")
    elif answer == "2":
        print("You try to obtain an illegal passport, but nobody sells any because North Korea is broke af. Soldiers catch you loitering around the airport and capture you. You are interrogated for betraying the dear leader and beat mercilessly :(")
    elif answer == "3":
        print("You are seen at the border and are shot immediately :(")
        restart()
