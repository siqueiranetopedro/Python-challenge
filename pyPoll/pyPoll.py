import csv,os



infile = "/Users/pedrosiqueira/election_data.csv"
outfile = "/Users/pedrosiqueira/election_results.txt"

total_number_vote = 0
vote_tally = {}
vote_list = []
winner = ""
winner_votes = 0

with open(infile) as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    csv_reader = next(csvreader)
    
   
    
    for row in csvreader:
        total_number_vote = total_number_vote + 1
        name = row[2]
        # print(name)
      
        if name in vote_tally:
            vote_tally[name] = vote_tally[name] + 1
        else: 
            vote_tally[name] = 1
            vote_list.append(name)
 
    print("Election Results")
    print()
    print("------------------------------")
    print()
    print("Total Votes:" , total_number_vote)
    print()
    print("------------------------------")
    print()
    
    Greatest_votes = 0
    
    for candidate in vote_tally:
        votes = vote_tally[candidate]
        vote_percentage = float(votes)/float(total_number_vote) * 100
        vote_percentage = round(vote_percentage,3)
        if votes > Greatest_votes:
            Greatest_votes = votes
            Greatest_votes_candidates = candidate
        print(f"{candidate} {vote_percentage}% ({votes})")
        print()
    print("------------------------------")
    print()
    print(Greatest_votes_candidates)
   
 
 
    
 
    #total number of votes
    # print("Total number of votes" , total_number_vote)

   
            
       
            
       
# output = (
#     f"Election Results\n"
#     f"-------------------------\n"
#     f"Total Votes: {total_number_vote} \n")
       
       
        
       
# print(output)

 
       
# with open(outfile,"w") as txtfile:
#     txtfile.write(output)
    




#     for candidate in vote_list:
        
#         votes = vote_tally.get(candidate)
#         vote_percentage = float(votes)/float(total_number_vote) * 100
        
#         if
        
        
#         output = f'{candidate}: {vote_percentage:.3f}% {votes}\n'
#         print(output)
#         txtfile.write(output)
      
      
     
      
      
      
      
      
      
      
    
            
         
            
  # # percentage each candidate won
  #   Charles_percentage_vote = 85213
  #   Total_votes = 369711
  #   Charles_percentage_vote = (Charles_percentage_vote / Total_votes ) * 100
  #   print("Charlers Percentage" , Charles_percentage_vote)
    
    
  #   diana_percentage_vote = 272892
  #   Total_votes = 369711
  #   diana_percentage_vote = (diana_percentage_vote / Total_votes ) * 100
  #   print("Diana Percentage" , diana_percentage_vote)
   
    
   
  #   raymon_percentage_vote = 11606
  #   Total_votes = 369711
  #   raymon_percentage_vote = (raymon_percentage_vote / Total_votes ) * 100
  #   print("Raymon Percentage" , raymon_percentage_vote)
  
            
  # #winner
  
  
  
   
    

    
    
 
 

