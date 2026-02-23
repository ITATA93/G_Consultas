# SQLUser.PA_PregDelBaby

**Schema:** SQLUser
**Columnas:** 189
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BABY_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| BABY_Abnormalities | varchar |  |  | SI | Baby Abnormalities |
| BABY_Accoucheur1_DR | varchar |  | FK | SI | Accoucheur 1 Des Ref CT_CareProv |
| BABY_Accoucheur2_DR | varchar |  | FK | SI | Accoucheur 2 Des ref CT_CareProv |
| BABY_ActualDelivPlaceComments | varchar |  |  | SI | Actual Delivery Place Comments |
| BABY_ActualDelivPlaceOth | varchar |  |  | SI | Actual Delivery place other |
| BABY_ActualDelivPlaceOth_DR | bigint |  | FK | SI | Des Ref PAC_DeliveryPlace |
| BABY_ActualDelivPlace_DR | bigint |  | FK | SI | Des Ref PAC_DeliveryPlace |
| BABY_AgeDeath | integer |  |  | SI | Age of Baby at time of Death Value |
| BABY_AgeDeathFactor | varchar |  |  | SI | Age of Baby at time of Death Unit |
| BABY_Alive | varchar |  |  | SI | Baby Alive |
| BABY_Anesthetist_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BABY_AnonymousDelivery | varchar |  |  | SI | [DEPRECATED]Field has been replaced by BABYAnonymo... |
| BABY_AnonymousDelivery_DR | bigint |  | FK | SI | Des Ref ORCAnonymousDelivery |
| BABY_ApgarScore1min_DR | bigint |  | FK | SI | Apgar score at 1 min Des res PAC_ApgarScore |
| BABY_ApgarScore3_DR | bigint |  | FK | SI | Apgar Score extra 1 Des Ref Apgar Score |
| BABY_ApgarScore4_DR | bigint |  | FK | SI | Apgar score extra 2 Des Ref Apgar Score |
| BABY_ApgarScore5min_DR | bigint |  | FK | SI | Apgar score at 5 min Des ref PAC_ApgarScore |
| BABY_ApgarTime3 | double |  |  | SI | Apgar score time extra 1 |
| BABY_ApgarTime4 | double |  |  | SI | Apgar Score extra 2 |
| BABY_ArtificiallyFed | varchar |  |  | SI | Artificially Fed |
| BABY_BabyFeedingType_DR | bigint |  | FK | SI | Des Ref PACBabyFeedingType |
| BABY_BabyLastName | varchar |  |  | SI | Baby Last Name |
| BABY_BabyName | varchar |  |  | SI | Baby First Name |
| BABY_BirthDate | date |  |  | SI | Birth Date |
| BABY_BirthDateAprxFlag | varchar |  |  | SI | Birth Date Approximate Flag |
| BABY_BirthLength | double |  |  | SI | Baby Length at Birth |
| BABY_BirthOrderNumber | double |  |  | SI | Birth Order Number |
| BABY_BirthPlaceChangeWhen_DR | bigint |  | FK | SI | Des Ref PAC_BirthPlaceChangeWhen |
| BABY_BirthWeigth | double |  |  | SI | Birth Weight |
| BABY_BornUnderwater | varchar |  |  | SI | Baby Born Underwater |
| BABY_BreastFed | varchar |  |  | SI | Breast Fed |
| BABY_BreastfedDurFactor | varchar |  |  | SI | Breastfed duration factor |
| BABY_BreastfedDuration | double |  |  | SI | Breastfed duration |
| BABY_Caput | varchar |  |  | SI | Caput |
| BABY_CervDilationMembranesRupt | double |  |  | SI | Cervical Dilation when Membranes Ruptures |
| BABY_Childsub | double |  |  | NO | Childsub |
| BABY_CongenitalAbnormalities | varchar |  |  | SI | Congenital Abnormalities |
| BABY_CordBldArtBaseExcess | double |  |  | SI | Cord Blood - Arterial Base Excess |
| BABY_CordBldBaseExcess | double |  |  | SI | Cord Blood - Base Excess |
| BABY_CordBldLactate | double |  |  | SI | Cord Blood Lactate |
| BABY_CordBldSentOther | varchar |  |  | SI | Cord Blood Sent - Other |
| BABY_CordBldSentRhNeg | varchar |  |  | SI | Cord Blood Sent as Rh Negative |
| BABY_CordBldVenBaseExcess | double |  |  | SI | Cord Blood - Venous Base Excess |
| BABY_CordBloodDonated | varchar |  |  | SI | CordBloodDonated |
| BABY_CordBloodDonated_DR | bigint |  | FK | SI | Des Ref PACReasonNotDonateCordBlood |
| BABY_CordBloodStoredPersUse | varchar |  |  | SI | CordBloodStoredPersUse |
| BABY_CordBloodStoredPersUse_DR | bigint |  | FK | SI | Des Ref PACReasonNotDonateCordBlood |
| BABY_CordClamp | varchar |  |  | SI | Delayed Cord Clamping |
| BABY_CordInsertion_DR | bigint |  | FK | SI | Cord Insertion |
| BABY_CordPHArterial | double |  |  | SI | Cord pH Arterial |
| BABY_CordPHVenous | double |  |  | SI | Cord pH Venous |
| BABY_CordRoundNeck | varchar |  |  | SI | Cord Round Neck |
| BABY_CordVessels_DR | bigint |  | FK | SI | Cord Vessels |
| BABY_CoreBloodLactArterial | double |  |  | SI | Core Blood Lactate Arterial |
| BABY_DateFirstContact | date |  |  | SI | Date of First Skin Contact |
| BABY_DateFirstFeed | date |  |  | SI | Date of First Feeding |
| BABY_DecisionMaker_DR | bigint |  | FK | SI | Decision Maker DR PACDelDecisionMaker |
| BABY_Defecation | varchar |  |  | SI | Defecation |
| BABY_DeliveryDoctor_DR | varchar |  | FK | SI | Delivery Doctor Des Ref CT_CareProv |
| BABY_DeliveryMidwife_DR | varchar |  | FK | SI | Delivery midwife Des ref CT_CareProv |
| BABY_DescBabyAtBirth | varchar |  |  | SI | Description of baby at birth |
| BABY_DischargeWeight | double |  |  | SI | Discharge weight |
| BABY_ECV_DR | bigint |  | FK | SI | External Cephalic Version |
| BABY_EntryID | varchar |  |  | SI | EntryID |
| BABY_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| BABY_ExcludeFromLC | varchar |  |  | SI | Exclude From Living Children |
| BABY_ExternGenital_DR | bigint |  | FK | SI | External Genitalia |
| BABY_FdiuDiagnosis | bigint |  |  | SI | When FDIU was diagnosed |
| BABY_Fetus_DR | varchar |  | FK | SI | The Fetus object associated with the Baby |
| BABY_FirstRespiration_DR | bigint |  | FK | SI | Des ref PAC_Respiration |
| BABY_FlyingSquad | varchar |  |  | SI | Flying squad |
| BABY_FormulaType_DR | bigint |  | FK | SI | DR Formula Type |
| BABY_FreeText1 | varchar |  |  | SI | FreeText1 |
| BABY_FreeText2 | varchar |  |  | SI | FreeText2 |
| BABY_FreeText3 | varchar |  |  | SI | FreeText3 |
| BABY_FreeText4 | varchar |  |  | SI | FreeText4 |
| BABY_GestationDays | double |  |  | SI | Gestation Days |
| BABY_GestationWeeks | double |  |  | SI | Gestation weeks |
| BABY_Gynecologist1_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BABY_Gynecologist2_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BABY_HepBGiven | varchar |  |  | SI | Hepatitis B vaccine given |
| BABY_HepBRefused | varchar |  |  | SI | Hepatitis B vaccine refused |
| BABY_IndigStatus_DR | bigint |  | FK | SI | Indigenous Status |
| BABY_LiquorColor_DR | bigint |  | FK | SI | Des Ref Liquor Colour |
| BABY_LivingArrangement_DR | bigint |  | FK | SI | Des Ref PACLivingArrangement  |
| BABY_MaconiumStain_DR | bigint |  | FK | SI | Des Ref PAC_MaconiumStain |
| BABY_Malformation | varchar |  |  | SI | Malformation |
| BABY_MembRuptureDate | date |  |  | SI | Membranes rupture date |
| BABY_MembRuptureDuration | varchar |  |  | SI | MembRuptureDuration |
| BABY_MembRuptureTime | time |  |  | SI | Membrane rupture time |
| BABY_Membranes_DR | bigint |  | FK | SI | Membranes |
| BABY_MotherPosition_DR | bigint |  | FK | SI | Position adopted by mother |
| BABY_Moulding | varchar |  |  | SI | Moulding |
| BABY_NeonatalIndicator_DR | bigint |  | FK | SI | Des Ref PAC_NeonatalIndicator |
| BABY_NeonateAutopsy_DR | bigint |  | FK | SI | Des Ref ORCNeonateAutopsy |
| BABY_NewbornPerson_DR | bigint |  | FK | SI | Newborn PAPerson |
| BABY_NewbornScrnTestDate | date |  |  | SI | Date newborn screening test done |
| BABY_NewbornScrnTestTime | time |  |  | SI | Time newborn screen test done |
| BABY_NndDate | date |  |  | SI | Date of neonatal death |
| BABY_NndTime | time |  |  | SI | Time of neonatal death |
| BABY_NoAutopsyReason_DR | bigint |  | FK | SI | Reason for Not Performing Autopsy |
| BABY_NoFirstContactReason_DR | bigint |  | FK | SI | Des Ref PAC_NoFirstSkinContactReason |
| BABY_NonCareProvDelivered | bigint |  |  | SI | Non-Care Provider Delivered the Baby |
| BABY_NonCareProvsPresentList | varchar |  |  | SI | Non Care Providers Present lookup to listbox  |
| BABY_Number1 | double |  |  | SI | Number1 |
| BABY_Number2 | double |  |  | SI | Number2 |
| BABY_ObsEntry_DR | varchar |  | FK | SI | Des Ref to MRObservations |
| BABY_OccipitoFrontalCircum | double |  |  | SI | Occipito Frontal Circumference |
| BABY_OpDelIndicationList | varchar |  |  | SI | Operative indicators lookup to listbox |
| BABY_OpDelIndicationText | varchar |  |  | SI | Operative Delivery Indication Free Text |
| BABY_OpDelIndication_DR | bigint |  | FK | SI | Operative Delivery Indication |
| BABY_OthCongAnom | varchar |  |  | SI | Other congenital anomalies |
| BABY_OthCordDetails | varchar |  |  | SI | Other Cord Details |
| BABY_OthDelMthd | varchar |  |  | SI | Other delivery methods |
| BABY_OthNeoMorb | varchar |  |  | SI | Other Neonatal morbidity |
| BABY_OthResusMth | varchar |  |  | SI | Other resuscitation methods |
| BABY_OtherStaffReg | varchar |  |  | SI | Other staff registration number |
| BABY_OutcomeFreeText | varchar |  |  | SI | Outcome Free Text |
| BABY_Outcome_DR | bigint |  | FK | SI | Des Ref PAC_OutcomeOfPregnancy |
| BABY_Pathologies | varchar |  |  | SI | [DEPRECATED]Field has been replaced by BABYPatholo... |
| BABY_PathologiesList | varchar |  |  | SI | Pathologies List |
| BABY_Pediatrician_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| BABY_PersonBeforeError_DR | bigint |  | FK | SI | Des Ref PAPerson Before Delivery Was Marked Entere... |
| BABY_Person_DR | bigint |  | FK | SI | Des Ref PAPerson |
| BABY_Position_DR | bigint |  | FK | SI | Positon of baby DR PAC_BabyPosition |
| BABY_PresentDuringDeliv_DR | bigint |  | FK | SI | Des Ref ORCPresentedDuringDelivery |
| BABY_Presentation | bigint |  |  | SI | Des Ref PAC_Presentation |
| BABY_PresentationLabour | bigint |  |  | SI | Baby Presentation at Labour Onset |
| BABY_PresentationText | varchar |  |  | SI | Presentation Free Text |
| BABY_QuantityOfLiquor_DR | bigint |  | FK | SI | Des Ref ORCQuantityofLiquor |
| BABY_ReasonDeath | varchar |  |  | SI | Reason for Death |
| BABY_Receiver1_DR | varchar |  | FK | SI | Receiver 1 Des ref CT_CareProv |
| BABY_Receiver2_DR | varchar |  | FK | SI | Receiver 2 Des Ref CT_CareProv |
| BABY_ResusciatedBy_DR | varchar |  | FK | SI | Resusciated By |
| BABY_ResuscitationOther | varchar |  |  | SI | Resuscitation Other |
| BABY_RowId | varchar |  |  | NO | - |
| BABY_Sex_DR | bigint |  | FK | SI | Des ref CTSex |
| BABY_SkinContactDur | numeric |  |  | SI | Duration of Skin Contact |
| BABY_SkinToSkinContactText | varchar |  |  | SI | Skin to Skin Contact Free Text |
| BABY_SkinToSkinContact_DR | bigint |  | FK | SI | Skin to Skin Contact |
| BABY_Text1 | varchar |  |  | SI | Text1 |
| BABY_Text10 | varchar |  |  | SI | Text10 |
| BABY_Text11 | varchar |  |  | SI | Text11 |
| BABY_Text12 | varchar |  |  | SI | Text12 |
| BABY_Text13 | varchar |  |  | SI | Text13 |
| BABY_Text14 | varchar |  |  | SI | Text14 |
| BABY_Text15 | varchar |  |  | SI | Text15 |
| BABY_Text16 | varchar |  |  | SI | Text16 |
| BABY_Text2 | varchar |  |  | SI | Text2 |
| BABY_Text3 | varchar |  |  | SI | Text3 |
| BABY_Text4 | varchar |  |  | SI | Text4 |
| BABY_Text5 | varchar |  |  | SI | Text5 |
| BABY_Text6 | varchar |  |  | SI | Text6 |
| BABY_Text7 | varchar |  |  | SI | Text7 |
| BABY_Text8 | varchar |  |  | SI | Text8 |
| BABY_Text9 | varchar |  |  | SI | Text9 |
| BABY_ThoracicCircumference | double |  |  | SI | Thoracic Circumference |
| BABY_TimeFirstContact | time |  |  | SI | Time of First Skin Contact |
| BABY_TimeFirstFeed | time |  |  | SI | Time of First Feeding |
| BABY_TimeOfBirth | time |  |  | SI | Time of birth |
| BABY_TimeToEstRespiration_DR | bigint |  | FK | SI | Time to estblsh resprtn PAC_Respiration |
| BABY_Transferred | bit |  |  | SI | Baby Transferred |
| BABY_TrueKnot | varchar |  |  | SI | True Knot |
| BABY_TypeOfMemberRupture_DR | bigint |  | FK | SI | Des Ref ORCTypeofMemberRupture |
| BABY_UpdateDate | date |  |  | SI | Last Update Date |
| BABY_UpdateHospital_DR | bigint |  | FK | SI | Last update hospital |
| BABY_UpdateTime | time |  |  | SI | Last Update Time |
| BABY_UpdateUser | bigint |  |  | SI | Last Update User |
| BABY_Urination | varchar |  |  | SI | Urination |
| BABY_VitKGiven | varchar |  |  | SI |  Vitamin K given - traditional field to document w... |
| BABY_VitKGiven_DR | bigint |  | FK | SI | Vitamin K Given - field to document whether Vitami... |
| BABY_YesNo1 | varchar |  |  | SI | YesNo1 |
| BABY_YesNo10 | varchar |  |  | SI | YesNo10 |
| BABY_YesNo11 | varchar |  |  | SI | YesNo11 |
| BABY_YesNo12 | varchar |  |  | SI | YesNo12 |
| BABY_YesNo13 | varchar |  |  | SI | YesNo13 |
| BABY_YesNo14 | varchar |  |  | SI | YesNo14 |
| BABY_YesNo15 | varchar |  |  | SI | YesNo15 |
| BABY_YesNo16 | varchar |  |  | SI | YesNo16 |
| BABY_YesNo2 | varchar |  |  | SI | YesNo2 |
| BABY_YesNo3 | varchar |  |  | SI | YesNo3 |
| BABY_YesNo4 | varchar |  |  | SI | YesNo4 |
| BABY_YesNo5 | varchar |  |  | SI | YesNo5 |
| BABY_YesNo6 | varchar |  |  | SI | YesNo6 |
| BABY_YesNo7 | varchar |  |  | SI | YesNo7 |
| BABY_YesNo8 | varchar |  |  | SI | YesNo8 |
| BABY_YesNo9 | varchar |  |  | SI | YesNo9 |
| Baby_CertOfGestation_DR | bigint |  | FK | SI | Des ref PAC_CertaintyOfGestation |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*