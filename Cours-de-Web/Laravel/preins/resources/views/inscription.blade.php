@extends('layouts.app')

@section('content')
    <form action="{{ url('inscription')}}" encrypt="multipart/form-data" autocomplete="off" method="post">
        <input type="hidden" name="_token" value="{{ csrf_token() }}">
    <label for="nom">Nom</label>
    <input type="text" name="nom" placeholder="Nom">
    <br>
    <label for="prenom">Prénom</label>
    <input type="text" name="prenom" placeholder="Prénom">
    <br>
    <label for="datenais">Date de naissance</label>
    <input type="date" name="datenais" placeholder="Date de naissance">
    <br>
    <label for="villenais">Ville de naissance</label>
    <input type="text" name="villenais" placeholder="Ville de naissance">
    <br>
    <input type="submit" value="M'inscrire">
    </form>
@endsection
