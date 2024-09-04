import re

################ file's functions
def get_dishes_names(f_read):
  names = []
  line_prev = False
  for line in (f_read):
    if line != '\n':
      if line_prev == False:
        names.append(line[:-1])
      line_prev = True
    else:
      line_prev = False

  return names
def get_count (f_read, names):
  count =[]
  line_prev = True
  for line in (f_read):
    if line[:-1] in names:
      line_prev = False
    else:
      if line_prev == False:
        count.append(int(line[:-1]))  # запись количества в массив в виде целого числа
        line_prev = True

  return count
def get_ingredients(f_read,count, names):
  ingredients_list =[]
  line_prev = True
  ingredients=[]
  quantity =[]
  measure =[]

  for line in (f_read):
    if line[:-1] in str(count):
      line_prev = False

    else:
      if line_prev == False and line != '\n' and (line[:-1] in names)==False:
        ingredients_list.append(line[:-1])
        words = [word.strip() for word in re.split(r's*\|s*',line[:-1])]   #разделение слов через разделитель |

        ingredients.append(words[0])
        quantity.append(words[1])
        measure.append(words[2])


      else:
        line_prev = True

  return ingredients, quantity, measure
def dict_write(names, count, ingredients, quantity, measure):
  cook_book = {}
  for i in range(len(names)):
    str_curr_list =[]
    for j in range(count[i]):
      str_curr ={}
      str_curr['ingredients']=ingredients[j]
      str_curr['quantity'] = quantity[j]
      str_curr['measure'] = measure[j]
      str_curr_list.append(str_curr)
    cook_book[names[i]]= str_curr_list

  return cook_book

################

############### processing and writing to dictionary

f_read = open("receipts.txt", encoding='UTF-8') # reading file
names = get_dishes_names(f_read)   # dishes names defining from file
print(names)

f_read = open("receipts.txt", encoding='UTF-8')
count = get_count(f_read, names)   # defining count of ingredients for dishes
print(count)

f_read = open("receipts.txt", encoding='UTF-8')
ingredients, quantity, measure = get_ingredients(f_read, count, names)
print(ingredients, quantity, measure)    # defining products, quantity of products and measure


dict_ = dict_write(names, count, ingredients, quantity, measure)  # dictionary form
print(dict_)

