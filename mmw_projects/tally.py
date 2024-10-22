
def tally_counting(class_num, data_min, data_max, limits, class_limits, data, equal=None):
  not_suitable = False
  somewhat_suitable = False
  tally = 0
  tally5 = 0
  i = 0

  for i in range(class_num):
    if i >= 1:
      lim_min = lim_max + 1
      lim_max = lim_min + limits

    else:
      lim_min = data_min
      lim_max = lim_min + limits


    for nums in data:
      if lim_min <= nums <= lim_max:
        tally += 1
        if tally == 5:
          tally5 += 1
          tally = 0

    if equal is True:
      if lim_max != data_max:
        not_suitable = True
      else:
        not_suitable = False

      if lim_max == data_max or lim_min > data_max:
        somewhat_suitable = True
      else:
        somewhat_suitable = False
    

    else: 
      if lim_min > data_max:
        not_suitable = True
        class_limits.append((lim_min, lim_max, tally5, tally, i))
        tally5 = 0
        tally = 0
      else:
        class_limits.append((lim_min, lim_max, tally5, tally, i))
        tally5 = 0
        tally = 0

    lim_min = data_min

  return (not_suitable, somewhat_suitable)


def tally(data: list, class_num=None, suitbale_class_limits=None):

  if (class_num is not None or suitbale_class_limits is not None) or (isinstance(class_num, int)):
    data_max = max(data)
    data_min = min(data)
    R = data_max - data_min
    class_limits = []
    ideal_limits = []
    somewhat_ideal = []
    not_Ideal = True

    if suitbale_class_limits is True:
      for i in range(4, 31):
        limits = R // i
        not_Ideal = tally_counting(i, data_min, data_max, limits, class_limits, data, equal=True)

        if not not_Ideal[0]:
          ideal_limits.append(i)
        if not not_Ideal[1]:
          somewhat_ideal.append(i)
        
      
      print("These Are The Suitable Class Limits:")
      for i in ideal_limits:
        print(i)

      print()
      print("These Are The Somewhat Suitable Class Limits: ") 
      for i in somewhat_ideal:
        print(i) 

    else:
      limits = R // class_num
      not_Ideal = tally_counting(class_num, data_min, data_max, limits, class_limits, data)

      if not_Ideal[0]:
        print("Not Ideal For This Data")
        choice = input("Do You Still Want to View (yes/no):").upper()

        if choice == "YES":
          for i in class_limits:
            print(f"{i[4] + 1}. {i[0]}-{i[1]} : {i[0]-0.5}-{i[1]+0.5} : {i[2]} 卌 - {i[3]}| : {int((((i[2]*5)+i[3])/len(data))*100)}%")

      else: 
      
        print("Class Limits : Class Boundaries : Tally : Percent ")


        for i in class_limits:
          print(f"{i[4] + 1}. {i[0]}-{i[1]} : {i[0]-0.5}-{i[1]+0.5} : {i[2]} 卌 - {i[3]}| : {int((((i[2]*5)+i[3])/len(data))*100)}%")
  
  else:
    print("Must Input A number")
    
if __name__=='__main__':

  data = [112, 100, 127, 120, 134, 118, 105, 110, 109, 112,
          110, 118, 117, 116, 118, 122, 114, 114, 105, 109,
          107, 112, 114, 115, 118, 117, 118, 122, 106, 110,
          116, 108, 110, 121, 113, 120, 119, 111, 104, 111,
          120, 113, 120, 117, 105, 110, 118, 112, 114, 114]
  
  tally(data, class_num=18)