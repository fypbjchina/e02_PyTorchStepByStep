
# Defines number of epochs
n_epochs = 200

losses = []

for epoch in range(n_epochs):
    # inner loop
    loss = mini_batch(device, train_loader, train_step_fn)
    losses.append(loss)

    # print loss every 20 epochs
    if epoch % 20 == 0:
        print(f'Epoch {epoch}/{n_epochs}, Loss: {loss}')
