@extends('layouts.app')
@section('name')
    <form action="/inscription" method="post">
        <label for="nom">Nom</label>
        <input type="text" name="nom" placeholder="Nom">
        <label for="prenom">Prenom</label>
        <input type="text" name="prenom" placeholder="Prenom">
        <label for="datenais">Date de naissance</label>
        <input type="text" name="datenais" placeholder="Date de naissance">
        <label for="villenais">Ville de naissance</label>
        <input type="text" name="villenais" placeholder="Ville de naissance">

    </form>

@endsection
