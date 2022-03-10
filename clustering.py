import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
#khoi tao du lieu
df =pd.DataFrame({
    'x':[12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72,85,88,87,91,74,76,71,69],
    'y':[39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14,69,68,72,74, 8, 19, 7, 24,82,83,96,89]
})
#print(df)
#print(len(df))
np.random.seed(200)
k = 5 #so cluster
centroids = {
    i+1 :[np.random.randint(0,100),np.random.randint(0,100)]
    for i in range(k)
}
#print(centroids)
#plot
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'red', 2: 'green', 3: 'blue',4:'orange',5:'purple'}
for i in centroids.keys():
    #print(centroids[i])
    plt.scatter(*centroids[i], color=colmap[i])
#plt.xlim(0,100)
#plt.ylim(0,100)
#plt.show()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering')

#tinh khoang cach tu point den centroids
def assign(df, centroids):
    for i in centroids.keys():
        #print(centroids[i][0])
        df['distancefrom_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )

    centroid_distance_cols = ['distancefrom_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distancefrom_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    #print(centroid_distance_cols)
    #print(df['color'])
    #print(df['closest'])
    return df

df =assign(df,centroids)
#print(df)

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
#plt.xlim(0,100)
#plt.ylim(0,100)
#plt.show()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering')

#update lai tam cua cluster

old_centroids = copy.deepcopy(centroids)
def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k
centroids = update(centroids)
#print(centroids)

fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
#    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering')

df = assign(df, centroids)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering')
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assign(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering')
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()




