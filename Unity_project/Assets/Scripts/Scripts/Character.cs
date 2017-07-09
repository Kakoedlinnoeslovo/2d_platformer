using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Character : MonoBehaviour {
	private SpriteRenderer sprite;
	private Animator animator;
	private Transform position;
	private CharState State{
		get { return (CharState)animator.GetInteger ("State");}
		set{ animator.SetInteger ("State", (int)value);}
	}


	void Start(){
		position = GetComponentInParent<Transform> ();
		sprite = GetComponentInChildren<SpriteRenderer> ();
		animator = GetComponent<Animator> ();
	}
	void Update(){

		State = CharState.Idle;
		Run ();

	}
		


	private void Run(){
			if (Input.GetKey (KeyCode.LeftArrow)) {
				sprite.flipX = true;
			}
			if (Input.GetKey (KeyCode.RightArrow)) {
				sprite.flipX = false;
			}		
			State = CharState.Run;

	}
}

public enum CharState{
	Idle,
	Run,
	Fall
}
