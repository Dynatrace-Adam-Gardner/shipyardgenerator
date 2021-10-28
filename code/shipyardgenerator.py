from num2words import num2words
import yaml

print("Starting Shipyard Generator...")
shipyard = {
  "apiVersion": "spec.keptn.sh/0.2.0",
  "kind": "Shipyard",
  "metadata": {
    "name": "generated-shipyard"
  },
  "spec": {}
}

# Build Stages
number_of_stages = None
while number_of_stages is None:
  number_of_stages = input("How many stages (environments) do you have? ")

  try:
    number_of_stages = int(number_of_stages)
  except:
    number_of_stages = None
    print('Got an invalid number of stages. Please use numbers. Try again...')

stages = list()
count = 1
while count <= number_of_stages:
  ordinal = num2words(count, to="ordinal_num")
  stage_name = input(f"Please enter the name of your {ordinal} environment: ")
  stages.append({ "name": stage_name})
  count += 1

# Add stages
shipyard['spec']['stages'] = stages

# Build Sequences per stage
for stage in shipyard['spec']['stages']:

  sequences_in_this_stage = list()

  number_of_sequences_in_stage = None
  while number_of_sequences_in_stage is None:
    number_of_sequences_in_stage = input(f"How many sequences do you have in {stage['name']}? ")

    try:
      number_of_sequences_in_stage = int(number_of_sequences_in_stage)
    except:
      number_of_sequences_in_stage = None
      print('Got an invalid number of sequences. Please use numbers. Try again...')
    
    count = 1
    while count <= number_of_sequences_in_stage:
      ordinal = num2words(count, to="ordinal_num")
      sequence_name = input(f"Please enter the name of your {ordinal} sequence in {stage['name']}: ")
      sequences_in_this_stage.append({ "name": sequence_name })
      count += 1
  
  #print(f"Got {len(sequences_in_this_stage)} for stage {stage['name']}")
  
  # Add sequences to stage
  stage['sequences'] = sequences_in_this_stage

# Add tasks to each sequence
for stage in shipyard['spec']['stages']:
  for sequence in stage['sequences']:
    tasks_for_this_sequence = list()

    number_of_tasks_in_sequence = None
    
    while number_of_tasks_in_sequence is None:
      number_of_tasks_in_sequence = input(f"How many tasks do you have in the {sequence['name']} sequence of {stage['name']}? ")
      try:
        number_of_tasks_in_sequence = int(number_of_tasks_in_sequence)
      except:
        number_of_tasks_in_sequence = None
        print('Got an invalid number of tasks in this sequence. Please use numbers. Try again...')
    
      count = 1
      while count <= number_of_tasks_in_sequence:
        ordinal = num2words(count, to="ordinal_num")
        task_name = input(f"Please enter the name of your {ordinal} task in {sequence['name']} of {stage['name']}: ")
        tasks_for_this_sequence.append({ "name": task_name })
        count += 1
  
    # Add tasks to sequence
    sequence['tasks'] = tasks_for_this_sequence
        

# Done. Print output
print('\n')
print('Output follows. Save this as shipyard.yaml')
print('\n\n')
print('---')
print(yaml.dump(shipyard))


#foo = num2words(4, to="ordinal_num")
#print(foo)
