import random

lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = "0123456789"
symbole = "!@#$%^&*()_+"

caractere = lettre + lettre.lower() + nombre + symbole
caractere_no_symbole = lettre + lettre.lower() + nombre

while True:
	longueurMDP = int(input("Entrez la longueur du mot de passe: "))
	nombreDeMDP = int(input("Entrez le nombre de mot de passe: "))
	symbole_oui_non = str(input("Voulez-vous des symboles dans le mot de passe? (oui/non): "))
	
	if symbole_oui_non == "oui":
		for x in range(0, nombreDeMDP):
			MDP = ""
			for x in range(0, longueurMDP):
				MDP += random.choice(caractere)
			print("Votre mot de passe est:",MDP)
	elif symbole_oui_non == "non":
		for x in range(0, nombreDeMDP):
			MDP = ""
			for x in range(0, longueurMDP):
				MDP += random.choice(caractere_no_symbole)
			print("Votre mot de passe est:", MDP)
	elif symbole_oui_non != "oui" or symbole_oui_non != "non":
		print("ERREUR")
		