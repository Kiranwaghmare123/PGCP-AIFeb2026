### Visualization (Decision Boundary)
    # =========================
    from matplotlib.colors import ListedColormap
    
    # Use only first 2 features for 2D visualization
    X_vis = X_train[:, :2]
    y_vis = y_train.values
    
    X1, X2 = np.meshgrid(
        np.arange(start=X_vis[:, 0].min() - 1, stop=X_vis[:, 0].max() + 1, step=0.01),
        np.arange(start=X_vis[:, 1].min() - 1, stop=X_vis[:, 1].max() + 1, step=0.01)
    )
    
    plt.contourf(
        X1, X2,
        model.predict(np.c_[X1.ravel(), X2.ravel(), np.zeros_like(X1.ravel())]).reshape(X1.shape),
        alpha=0.75,
        cmap=ListedColormap(('red', 'green'))
    )
    
    plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y_vis, cmap=ListedColormap(('red', 'green')))
    plt.title('Decision Tree (Training set)')
    plt.xlabel('Age (scaled)')
plt.ylabel('Salary (scaled)')
plt.show()
