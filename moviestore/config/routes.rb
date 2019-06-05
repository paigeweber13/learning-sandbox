Rails.application.routes.draw do
  root 'movies#index'
  resources :movies, only: [:show, :index]
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
