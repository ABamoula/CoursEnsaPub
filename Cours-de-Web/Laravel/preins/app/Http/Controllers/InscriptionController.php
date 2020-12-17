<?php

namespace App\Http\Controllers;

use App\Models\inscription;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class InscriptionController extends Controller
{
    public function enginscription(Request $request){
        if(Auth::check()){
            $inscriptions = inscription::where('id_ind',Auth::user()-> id)->get();
            if($inscriptions->count()>0){
                $inscriptions = new inscription();
            DB::table('inscriptions')
                ->where('id_ind', Auth::user()->id)
                ->update(['nom' =>request('nom'),
                'prenom'=>request('prenom'),
                'datenais'=>request('datenais'),
                'villenais'=>request('villenais'),

                ]);



    } else {


        $inscription = new inscription();

        $inscription->id_ind = Auth::user()->id;
        $inscription->nom = request('nom');
        $inscription->prenom = request('prenom');
        $inscription->datenais = request('datenais');
        $inscription->villenais = request('villenais');
        $inscription->save();

    }

        return redirect('/inscription');
} else {

    return redirect('/login')->withErrors(['email' => "Vous devez être connecte pour voir cette page.",]);
}



    }


    public function affinscription(){
        try {
            if (Auth::check()) {
            // the code goes here
        $inscriptions=DB::table('inscriptions')
        ->select('inscriptions.nom','inscriptions.prenom','inscriptions.datenais','inscriptions.villenais')
        ->where('inscriptions.id_ind', Auth::user()->id)->get();
        return view('inscription',compact('inscriptions'));
            }
            else {

                return redirect('/login')->withErrors(['email' => "Vous devez être connecte pour voir cette page.",]);
            }
    } catch (Exception $e) {
        // if an exception happened in the try block above
        return redirect('/login');
    }

         }
}
