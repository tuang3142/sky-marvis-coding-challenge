require "rails_helper"

feature "User completes todo" do
  scenario "successfully" do
    sign_in

    create_todo "Standing desk"

    click_on "Mark as completed"

    expect(page).to display_completed_todo "Standing desk"
  end
end

