
# Defines number of epochs
n_epochs = 1000

losses = []

# For each epoch...
for epoch in range(n_epochs):
    # Performs one train step and returns the corresponding loss
    loss = train_step_fn(x_train_tensor, y_train_tensor)
    losses.append(loss)

    # when loss_next is bigger than loss_current, stop the training
    #if epoch > 0 and losses[epoch] > losses[epoch - 1]:
        #break

    # Prints the loss for every 100 epochs
    if epoch % 100 == 0:
        print(f'Epoch {epoch}/{n_epochs}, Loss: {loss}')
