# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:55:57 2022

@author: Yee Meng
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def provide_recommenation():
    # list of dog breeds
    dogs = ['Cavalier King Charles Spaniel', 'Boxer', 'English Springer Spaniel', 'Papillon', 'Poodle', 
    'Shih Tzu', 'Soft Coated Wheaten Terrier', 'Whippet', 'Labrador Retriever', 'Golden Retriever', 
    'Bichon Frise', 'Yorkshire Terrier', 'Pug', 'Bernese Mountain Dog', 'Great Dane', 
    'Pomeranian', 'Maltese', 'German Shepherd Dog', 'Cardigan Welsh Corgi', 'Chihuahua']
    
    if request.method == 'POST':
        # get the parameters
        param_1 = request.form['Housing'].casefold()
        param_2 = request.form['Kids'].casefold()
        param_3 = request.form['Noise_tolerance'].casefold()
        param_4 = request.form['Shedding_tolerance'].casefold()
        param_5 = request.form['Activity_level'].casefold()
        
        to_remove = {'dummy'}
        # question 1: What is your home like?
        if param_1 == 'hdb':
            to_remove.add('Boxer')
            to_remove.add('Poodle')
            to_remove.add('Soft Coated Wheaten Terrier')
            to_remove.add('Whippet')
            to_remove.add('Labrador Retriever')
            to_remove.add('Golden Retriever')
            to_remove.add('Bernese Mountain Dog')
            to_remove.add('Great Dane')
            to_remove.add('German Shepherd Dog')
        
        # question 2: Do you have kids under age 10?
        if param_2 == 'yes':
            to_remove.add('English Springer Spaniel')
            to_remove.add('Soft Coated Wheaten Terrier')
            to_remove.add('Whippet')
            to_remove.add('Yorkshire Terrier')
            to_remove.add('Pug')
            to_remove.add('Bernese Mountain Dog')
            to_remove.add('Great Dane')
            to_remove.add('Pomeranian')
            to_remove.add('Maltese')
            to_remove.add('Cardigan Welsh Corgi')
            to_remove.add('Chihuahua')
            
        # question 3: What is your noise tolerance for barking?
        if param_3 == 'medium':
            to_remove.add('Papillon')
            to_remove.add('Cardigan Welsh Corgi')
            to_remove.add('Chihuahua')
            
        # question 4: What is your tolerance for shedding?
        if param_4 == 'low':
            to_remove.add('Labrador Retriever')
            to_remove.add('Golden Retriever')
            to_remove.add('Pug')
            to_remove.add('Bernese Mountain Dog')
            to_remove.add('German Shepherd Dog')
            
        # question 5: What’s your activity level?
        if param_5 == 'low':
            to_remove.add('English Springer Spaniel')
            to_remove.add('Papillon')
            to_remove.add('Shih Tzu')
            to_remove.add('Soft Coated Wheaten Terrier')
            to_remove.add('Whippet')
            to_remove.add('Labrador Retriever')
            to_remove.add('Golden Retriever')
            to_remove.add('Bichon Frise')
            to_remove.add('Yorkshire Terrier')
            to_remove.add('Pug')
            to_remove.add('Bernese Mountain Dog')
            to_remove.add('Pomeranian')
            to_remove.add('Maltese')
            to_remove.add('German Shepherd Dog')
            to_remove.add('Chihuahua')
        elif param_5 == 'high':
            to_remove.add('Cavalier King Charles Spaniel')
            to_remove.add('Boxer')
            to_remove.add('Poodle')
            to_remove.add('Great Dane')
            to_remove.add('Cardigan Welsh Corgi')
        
        to_remove.remove('dummy')
        for dog in to_remove:
            dogs.remove(dog)
            
        # return
        return jsonify({'Breed': dogs})
    else:
        test = 'HDB'
        test.casefold()
        return jsonify({'Text': test})