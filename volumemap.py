# make a dictionary where the keys are the VolumeId and values are Author and Title
volumeMap = {
	"file:///mnt/onboard/Mills, C. Wright/Sociological Imagination, The - C. Wright Mills.epub": {
		"Author": "Mills, C. Wright",
		"Title": "Sociological Imagination, The"
	},
	"file:///mnt/onboard/Fisher, Mark/Capitalist Realism - Mark Fisher.epub": {
		"Author": "Fisher, Mark",
		"Title": "Capitalist Realism"
	},
	"file:///mnt/onboard/Anderson, Elijah/Code of the Street - Elijah Anderson.epub": {
		"Author": "Anderson, Elijah",
		"Title": "Code of the Street"
	},
	'file:///mnt/onboard/Said, Edward W_/Orientalism - Edward W. Said.epub': {
		"Author": "Said, Edward W.",
		"Title": "Orientalism"
	},
	'file:///mnt/onboard/Figes, Orlando/Crimean War, The - Orlando Figes.epub': {
		"Author": "Figes, Orlando",
		"Title": "Crimean War, The"
	},
	'file:///mnt/onboard/Parenti, Michael/Blackshirts and Reds_ Rational Fascism and the Overthrow of Communism - Michael Parenti.epub': {
		"Author": "Parenti, Michael",
		"Title": "Blackshirts and Reds: Rational Fascism and the Overthrow of Communism"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Last Kingdom, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Last Kingdom, The"
	},
	'file:///mnt/onboard/Tacitus & Tacitus & Mattingly, Harold & Rives, J.B_/Agricola and the Germania - Tacitus & Harold Mattingly & J.B. Rives.epub': {
		"Author": "Tacitus",
		"Title": "Agricola and the Germania"
	},
	'file:///mnt/onboard/Wright, Richard/Black Boy - Richard Wright.epub': {
		"Author": "Wright, Richard",
		"Title": "Black Boy"
	},
	'file:///mnt/onboard/Ludlum, Robert/Bourne Identity, The - Robert Ludlum.epub': {
		"Author": "Ludlum, Robert",
		"Title": "Bourne Identity, The"
	},
	'file:///mnt/onboard/Fukuyama, Francis/Origins of Political Order, The - Fukuyama, Francis.epub': {
		"Author": "Fukuyama, Francis",
		"Title": "Origins of Political Order, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Pale Horseman, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Pale Horseman, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Lords of the North, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Lords of the North, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Sword Song - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Sword Song"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Burning Land, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Burning Land, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Death of Kings - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Death of Kings"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Pagan Lord, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Pagan Lord, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Empty Throne, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Empty Throne, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Warriors of the Storm - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Warriors of the Storm"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Flame Bearer, The - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Flame Bearer, The"
	},
	'file:///mnt/onboard/Cornwell, Bernard/War of the Wolf - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "War of the Wolf"
	},
	'file:///mnt/onboard/Cornwell, Bernard/Sword of Kings - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "Sword of Kings"
	},
	'file:///mnt/onboard/Cornwell, Bernard/War Lord - Bernard Cornwell.epub': {
		"Author": "Cornwell, Bernard",
		"Title": "War Lord"
	},
	'file:///mnt/onboard/Graves, Robert/I, Claudius - Robert Graves.epub': {
		"Author": "Graves, Robert",
		"Title": "I, Claudius"
	},
	'file:///mnt/onboard/Coker, Margaret/Spymaster of Baghdad, The - Margaret Coker.epub': {
		"Author": "Coker, Margaret",
		"Title": "Spymaster of Baghdad, The"
	},
	'file:///mnt/onboard/Norwich, John Julius/Byzantium_ The Early Centuries - John Julius Norwich.epub': {
		"Author": "Norwich, John Julius",
		"Title": "Byzantium: The Early Centuries"
	},
	'file:///mnt/onboard/Miller, Madeline/Circe - Madeline Miller.epub': {
		"Author": "Miller, Madeline",
		"Title": "Circe"
	},
	'file:///mnt/onboard/Abnett, Dan/Horus Rising - Dan Abnett.epub': {
		"Author": "Abnett, Dan",
		"Title": "Horus Rising"
	},
	'file:///mnt/onboard/McNeill, Graham/False Gods - Graham McNeill.epub': {
		"Author": "McNeill, Graham",
		"Title": "False Gods"
	},
	'file:///mnt/onboard/Graeber, David/Debt - David Graeber.epub': {
		"Author": "Graeber, David",
		"Title": "Debt: The First 5,000 Years"
	},
	'file:///mnt/onboard/Admiral William H. McRaven/Sea Stories - William H. Mcraven.epub': {
		"Author": "McRaven, William H.",
		"Title": "Sea Stories: My Life in Special Operations"
	},
	'file:///mnt/onboard/Price, Neil/Children of Ash and Elm_ A History of the Vikings - Neil Price.epub': {
		"Author": "Price, Neil",
		"Title": "Children of Ash and Elm: A History of The Vikings"
	},
	'file:///mnt/onboard/Weir, Andy/Project Hail Mary - Andy Weir.epub': {
		"Author": "Weir, Andy",
		"Title": "Project Hail Mary"
	},
	'file:///mnt/onboard/Wohlleben, Peter/The Hidden Life of Trees_ What They Feel, How They CommunicateDiscoveries from a Secret World - Peter Wohlleben.epub': {
		"Author": "Wohlleben, Peter",
		"Title": "The Hidden Life of Trees"
	},
	'file:///mnt/onboard/Bradford, Ernle/Great Siege_ Malta 1565, The - Ernle Bradford.epub': {
		"Author": "Bradford, Ernle",
		"Title": "Great Siege: Malta 1565, The"
	},
	'file:///mnt/onboard/MacLean, Fitzroy/Eastern Approaches - Fitzroy MacLean.epub': {
		"Author": "MacLean, Fitzroy",
		"Title": "Eastern Approaches"
	},
	'file:///mnt/onboard/Ehrman, Bart D_/How Jesus Became God_ The Exaltation of a Jewish Preacher From Galilee - Bart D. Ehrman.epub': {
		"Author": "Ehrman, Bart D.",
		"Title": "How Jesus Became God: The Exaltation of a Jewish Preacher from Galilee"
	},
	'file:///mnt/onboard/X, Malcolm & Haley, Alex/Autobiography of Malcolm X, The - Malcolm X & Alex Haley.epub': {
		"Author": "X, Malcolm",
		"Title": "Autobiography of Malcolm X, The"
	},
	'file:///mnt/onboard/Norwich, John Julius/Byzantium_ The Apogee - John Julius Norwich.epub': {
		"Author": "Norwich, John Julius",
		"Title": "Byzantium: The Apogee"
	},
	'file:///mnt/onboard/Eco, Umberto/Foucault_s Pendulum - Umberto Eco.epub': {
		"Author": "Eco, Umberto",
		"Title": "Foucault's Pendulum"
	},
	'file:///mnt/onboard/Forsyth, Mark/Etymologicon, The - Mark Forsyth.epub': {
		"Author": "Forsyth, Mark",
		"Title": "Etymologicon, The"
	},
	'file:///mnt/onboard/Iggulden, Conn/Khan Series, The - Conn Iggulden.epub': {
		"Author": "Iggulden, Conn",
		"Title": "Khan Series, The"
	},
	'c7740ad8-4e7d-4201-947d-d34e200fb6f1': {
		"Author": "Eco, Umberto",
		"Title": "Foucault's Pendulum"
	},
	'file:///mnt/onboard/Pynchon, Thomas/Crying of Lot 49, The - Thomas Pynchon.epub': {
		"Author": "Pynchon, Thomas",
		"Title": "Crying of Lot 49, The"
	},
	'file:///mnt/onboard/Liu, Ken/Grace of Kings, The - Ken Liu.epub': {
		"Author": "Liu, Ken",
		"Title": "Grace of Kings, The"
	},
	
}