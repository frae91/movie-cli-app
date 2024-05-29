# Movie CLI App

## Models
### Movie, Genre, MovieGenre, Actor, Cast, User, Fave

## Relationships
`Movie` has many `Genre`s, through `MovieGenre`
`Movie` has many `Actor`s, through `Cast`
`Movie` has many `User`s, through `Fave`
`Actor` has many `Movie`s, through `Cast`
`User` has many `Movie`s, through `Fave`