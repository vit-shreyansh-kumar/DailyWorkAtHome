def center_to_origin(to_centered):
    for j in range(to_centered.shape[1]):
        mean_x = 0
        mean_y = 0
        for i in range(to_centered.shape[0]):
            if i%2==0:
                mean_x = mean_x + np.mean(to_centered[i, j])
            else:
                mean_y = mean_y + np.mean(to_centered[i, j])
        mean_x = mean_x/(40)
        mean_y = mean_y/(40)
        for i in range(to_centered.shape[0]):
            if i%2==0:
                to_centered[i, j] = to_centered[i, j] - mean_x
            else:
                to_centered[i, j] = to_centered[i, j] - mean_y
    return to_centered

landmarks_per_tooth = [1,2,3,5,6,7,8,9]
index =1
temp = landmarks_per_tooth[index]
print(landmarks_per_tooth[index][:, 1])
temp = center_to_origin(landmarks_per_tooth[index])
print(landmarks_per_tooth[index][:, 1])