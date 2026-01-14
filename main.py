
import random
import time

words = ('electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop'
        'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power',
        'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism',
        'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
        'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language',
        'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus',
        'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
        'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard',
        'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
        'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
        'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
        'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
        'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
        'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
        'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete',
        'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive',
        'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure',
        'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter',
        'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy'
        'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship',
        'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert',
        'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment',
        'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion',
        'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation'
        'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future',
        'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection', 'occupy'
        'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion',
        'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn',
        'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment',
        'permission', 'logic', 'analysis', 'password', 'english', 'equalizer', 'simulation'
        'emotion', 'battle', 'expression', 'scissors', 'trousers', 'glasses', 'department'
        'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health',
        'disaster', 'volcano', 'poverty', 'limitation', 'perfect', 'intelligence', 'infinity'
        'failure', 'ignorance', 'destination', 'source', 'resort', 'satisfaction', 'example'
        'frequency', 'selection', 'substitution', 'kingdom', 'pattern', 'management',
        'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet',
        'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object',
        'happen', 'happiness', 'worry', 'method', 'tolerance', 'error', 'hesitation',
        'record', 'tongue', 'supply', 'vibration', 'stress', 'despair', 'restaurant',
        'television', 'video', 'audio', 'layer', 'mixture', 'doorbell', 'cousin', 'beard'
        'finance', 'production', 'invisible', 'excitement', 'afternoon', 'office', 'alphabet'
        'illustration', 'valley', 'apartment', 'necessary', 'shortage', 'almost', 'furniture'
        'blanket', 'suggestion', 'overflow', 'demonstration', 'challenge', 'compact', 'kitten'
        'tower', 'question', 'problem', 'pressure', 'beast', 'encouragement', 'afraid',
        'cavity', 'appearance', 'wonderful', 'matter', 'dimension', 'business', 'doubt',
        'conversation', 'reaction', 'psychology', 'superstition', 'smash', 'horseshoe',
        'surprise', 'nothing', 'ladder', 'opposite', 'reality', 'genius', 'string', 'disengage'
        'destruction', 'expensive', 'painting', 'chicken', 'wishing', 'profession', 'engagement'
        'hatred', 'possession', 'criticism', 'zebra', 'harmony', 'personality', 'overcome'
        'addition', 'subtraction', 'cipher', 'encryption', 'compression', 'extension',
        'blessing', 'meeting', 'difficulty', 'weapon', 'against', 'external', 'internal',
        'legend', 'servant', 'secondary', 'license', 'directory', 'statistics',
         'attraction', 'sensitivity', 'magnification', 'someone', 'symptom', 'recipe',
        'service', 'family', 'island', 'planet', 'butterfly', 'diving', 'strength', 'misunderstood'
        'extreme', 'opportunity', 'illumination', 'cable', 'conflict', 'interference',
        'receiver', 'transmitter', 'channel', 'company', 'grocery', 'devil', 'angel',
        'exactly', 'document', 'tutorial', 'sound', 'voice', 'abbreviation', 'abdomen',
        'abrupt', 'absolute', 'absorption', 'abstract', 'academy', 'acceleration', 'access'
        'accident', 'account', 'acidification', 'actress', 'adaptation', 'addiction',
        'adjustment', 'admiration', 'adoption', 'advanced', 'adventure', 'advertisement',
        'agenda', 'airport', 'algorithm', 'allocation', 'aluminium', 'ambiguity', 'ambitious'
        'amphibian', 'anaesthesia', 'analogy', 'anchor', 'animation', 'anode', 'cathode',
        'apparent', 'appendix', 'approval', 'approximation', 'arbitrary', 'architecture',
        'arithmetic', 'arrangement', 'article', 'ascending', 'ashamed', 'asleep', 'assassinate'
        'assembly', 'astonishment', 'atmosphere', 'awful', 'bachelor', 'backbone', 'background'
        'bacteria', 'balance', 'balloon', 'banana', 'barbecue', 'baseball', 'beaker',
        'beggar', 'behaviour', 'benefit', 'bidirectional', 'biology', 'blackboard', 'blackened'
        'bladder', 'bleeding', 'blender', 'bonus', 'bottle', 'bracket', 'branch', 'brilliantly'
        'bubble', 'bucket', 'budget', 'bullet', 'burglar', 'butcher', 'bypass', 'cafeteria'
        'calculator', 'calibration', 'campaign', 'cancellation', 'candidate', 'candle',
        'carpenter', 'carriage', 'cartoon', 'cascade', 'casual', 'catalyst', 'category',
        'cement', 'ceremony', 'chairman', 'checkout', 'chimney', 'chocolate', 'cigarette'
        'circumference', 'civilization', 'classroom', 'clearance', 'client', 'coconut',
        'coincidence', 'colleague', 'comfortable', 'competition', 'kangaroo', 'kidnap',
        'journal', 'jockey', 'iteration', 'isometric', 'isolation', 'invitation', 'interstellar'
        'institution', 'injection', 'humanity', 'housekeeper', 'history', 'heaven', 'guitar'
        'greenhouse', 'glory', 'foundation', 'formula', 'fluctuation', 'fiction', 'extraordinary'
        'emission', 'elasticity', 'earthquake', 'dynamic', 'doctorate', 'divorce', 'derivative'
        'nightmare', 'virtue', 'description')

hangman_art = { 0:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃       ",
                   " ┃       ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                1:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃       ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                2:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃   │   ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                3:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│   ",
                   " ┃       ",
                   "━┻━━━━━━━"),
               4: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃       ",
                   "━┻━━━━━━━"),
               5: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃  ╱    ",
                   "━┻━━━━━━━"),
               6: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃  ╱ ╲  ",
                   "━┻━━━━━━━")
               }

def display_man(wrong_guesses):
    time.sleep(1)
    print("******************")
    time.sleep(0.3)
    for line in hangman_art[wrong_guesses]:
        print(line)
    time.sleep(0.3)
    print("******************")
    time.sleep(1)

def display_hint(hint):
    time.sleep(1)
    print(" ".join(hint))

def display_answer(answer):
    time.sleep(1)
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        time.sleep(1)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            time.sleep(1)
            print("Invalid input")
            continue

        if guess in guessed_letters:
            time.sleep(1)
            print(f"You already typed {guess}, try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("******************")
            print("You Win! Thank you for playing!")
            print("******************")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("******************")
            print("You Lose! Thank you for playing!")
            print("******************")
            is_running = False

if __name__ == "__main__":
    main()