require "rails_helper"

feature "User marks todo as incomplete" do
  scenario "successfully" do
    sign_in

    create_todo "Standing desk"

    click_on "Mark as completed"
    click_on "Mark as incompleted"

    expect(page).to display_todo "Standing desk"
  end
end
