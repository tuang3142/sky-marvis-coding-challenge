require "rails_helper"

feature "User sees todos" do
  scenario "doesn't see others' todos" do
    Todo.create!(title: "Buy milk", email: "not_me@example.com")

    sign_in_as "me@example.com"

    expect(page).not_to display_todo "Buy milk"
  end
end
