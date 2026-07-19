def weekly_training():


    download_data()


    create_features()


    train_xgboost()


    train_lstm()


    validate_models()


    if performance_good():

        deploy_model()
