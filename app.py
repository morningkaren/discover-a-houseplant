from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pickle
import numpy as np
import pandas as pd
import os
import random

with open('description.pkl', 'rb') as d:
    x_new = pickle.load(d)

with open('rec_matrix.pkl', 'rb') as j:
    rec_matrix = pickle.load(j)

def get_rec(plant):
 	return list(rec_matrix[plant].sort_values(ascending=False).head(6).tail(5).index)

plant1 = random.choice(x_new['title'])
index1 = x_new[x_new['title'] == plant1].index[0]
x_new1 = x_new.drop(index1)
plant2 = random.choice(x_new1['title'])
index2 = x_new1[x_new1['title'] == plant2].index[0]
x_new2 = x_new1.drop(index2)
plant3 = random.choice(x_new2['title'])
index3 = x_new2[x_new2['title'] == plant3].index[0]

fn0_1 = get_rec(plant1)[0]
fn1_1 = get_rec(plant1)[1]
fn2_1 = get_rec(plant1)[2]
fn3_1 = get_rec(plant1)[3]
fn4_1 = get_rec(plant1)[4]

fn0_2 = get_rec(plant2)[0]
fn1_2 = get_rec(plant2)[1]
fn2_2 = get_rec(plant2)[2]
fn3_2 = get_rec(plant2)[3]
fn4_2 = get_rec(plant2)[4]

fn0_3 = get_rec(plant3)[0]
fn1_3 = get_rec(plant3)[1]
fn2_3 = get_rec(plant3)[2]
fn3_3 = get_rec(plant3)[3]
fn4_3 = get_rec(plant3)[4]

idx_des0_1 = x_new[x_new['title'] == fn0_1].index[0]
idx_des1_1 = x_new[x_new['title'] == fn1_1].index[0]
idx_des2_1 = x_new[x_new['title'] == fn2_1].index[0]
idx_des3_1 = x_new[x_new['title'] == fn3_1].index[0]
idx_des4_1 = x_new[x_new['title'] == fn4_1].index[0]

idx_des0_2 = x_new[x_new['title'] == fn0_2].index[0]
idx_des1_2 = x_new[x_new['title'] == fn1_2].index[0]
idx_des2_2 = x_new[x_new['title'] == fn2_2].index[0]
idx_des3_2 = x_new[x_new['title'] == fn3_2].index[0]
idx_des4_2 = x_new[x_new['title'] == fn4_2].index[0]

idx_des0_3 = x_new[x_new['title'] == fn0_3].index[0]
idx_des1_3 = x_new[x_new['title'] == fn1_3].index[0]
idx_des2_3 = x_new[x_new['title'] == fn2_3].index[0]
idx_des3_3 = x_new[x_new['title'] == fn3_3].index[0]
idx_des4_3 = x_new[x_new['title'] == fn4_3].index[0]

PLANTS_FOLDER = os.path.join('static', 'plants_folder')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PLANTS_FOLDER


@app.route('/')
@app.route('/webpage')
def show_webpage():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{plant1}')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], f'{plant2}')
    full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], f'{plant3}')
    return render_template("webpage.html", user_image = full_filename,
                            user_image2 = full_filename2,
                            user_image3 = full_filename3,
                            plant1 = plant1, plant2 = plant2, plant3 = plant3,
                            description1 = x_new.iloc[index1, 1],
                            description2 = x_new.iloc[index2, 1],
                            description3 = x_new.iloc[index3, 1])

@app.route('/function')
def result():
    fn0 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant1)[0]}')
    fn1 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant1)[1]}')
    fn2 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant1)[2]}')
    fn3 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant1)[3]}')
    fn4 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant1)[4]}')
    return render_template("webpage2.html", result_image0 = fn0, result_image1 = fn1,
                            result_image2 = fn2, result_image3 = fn3, result_image4 = fn4,
                            fn0 = fn0_1, fn1 = fn1_1, fn2 = fn2_1 ,fn3 = fn3_1,
                            fn4 = fn4_1,
                            des0 = x_new.iloc[idx_des0_1, 1], des1 = x_new.iloc[idx_des1_1, 1],
                            des2 = x_new.iloc[idx_des2_1, 1], des3 = x_new.iloc[idx_des3_1, 1],
                            des4 = x_new.iloc[idx_des4_1, 1])

@app.route('/function2')
def result2():
    fn0 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant2)[0]}')
    fn1 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant2)[1]}')
    fn2 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant2)[2]}')
    fn3 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant2)[3]}')
    fn4 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant2)[4]}')
    return render_template("webpage2.html", result_image0 = fn0, result_image1 = fn1,
                            result_image2 = fn2, result_image3 = fn3, result_image4 = fn4,
                            fn0 = fn0_2, fn1 = fn1_2, fn2 = fn2_2 ,fn3 = fn3_2,
                            fn4 = fn4_2,
                            des0 = x_new.iloc[idx_des0_2, 1], des1 = x_new.iloc[idx_des1_2, 1],
                            des2 = x_new.iloc[idx_des2_2, 1], des3 = x_new.iloc[idx_des3_2, 1],
                            des4 = x_new.iloc[idx_des4_2, 1])

@app.route('/function3')
def result3():
    fn0 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant3)[0]}')
    fn1 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant3)[1]}')
    fn2 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant3)[2]}')
    fn3 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant3)[3]}')
    fn4 = os.path.join(app.config['UPLOAD_FOLDER'], f'{get_rec(plant3)[4]}')
    return render_template("webpage2.html", result_image0 = fn0, result_image1 = fn1,
                            result_image2 = fn2, result_image3 = fn3, result_image4 = fn4,
                            fn0 = fn0_3, fn1 = fn1_3, fn2 = fn2_3 ,fn3 = fn3_3,
                            fn4 = fn4_3,
                            des0 = x_new.iloc[idx_des0_3, 1], des1 = x_new.iloc[idx_des1_3, 1],
                            des2 = x_new.iloc[idx_des2_3, 1], des3 = x_new.iloc[idx_des3_3, 1],
                            des4 = x_new.iloc[idx_des4_3, 1])


if __name__ == '__main__':
    app.run(debug = True)
