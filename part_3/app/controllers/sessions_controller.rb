class SessionsController < ApplicationController
  def new
  end

  def create
    sign_in_as params[:session][:email]
    redirect_to root_url
  end
end

