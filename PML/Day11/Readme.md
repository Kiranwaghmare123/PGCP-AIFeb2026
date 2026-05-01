## Visualization

    def plot_decision_boundary(X_set, y_set, title):
        X1, X2 = np.meshgrid(
            np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
            np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01)
        )
    
        plt.figure()
        plt.contourf(
            X1, X2,
            classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
            alpha=0.3
        )
    
        for i, j in enumerate(np.unique(y_set)):
            plt.scatter(
                X_set[y_set == j, 0],
                X_set[y_set == j, 1],
                label=j
            )
