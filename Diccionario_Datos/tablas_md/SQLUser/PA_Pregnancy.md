# SQLUser.PA_Pregnancy

**Schema:** SQLUser
**Columnas:** 194
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREG_RowId | bigint | PK |  | NO | - |
| PREG_AntenatalCare_DR | bigint |  | FK | SI | Antenatal Care DR PACTypeOFAntenatalCare |
| PREG_AntenatalClassType_DR | varchar |  | FK | SI | Des Ref PAPregAntenClassType |
| PREG_AntenatalClass_DR | varchar |  | FK | SI | Des Ref PAPregAntenClass |
| PREG_Antibodies | varchar |  |  | SI | Antibodies present |
| PREG_Art | varchar |  |  | SI | Artificial reproductive technologies |
| PREG_BishopScore | double |  |  | SI | Bishop Score  |
| PREG_BleedingSinceLMP | varchar |  |  | SI | Bleeding since LMP |
| PREG_BookingChangeManag_DR | bigint |  | FK | SI | Des ref PAC_BookingChangeManag |
| PREG_BookingChangePlace_DR | bigint |  | FK | SI | Des Ref PAC_BookingChangePlace |
| PREG_BookingGestation | varchar |  |  | SI | Gestation at Booking |
| PREG_CMatCaesarean | double |  |  | SI | CMatCaesarean |
| PREG_CPNotified | varchar |  |  | SI | Associated Care Providers Notified of Change |
| PREG_CancelReason_DR | bigint |  | FK | SI | Cancellation Reason DR PAC_ReasonPregCancel |
| PREG_CareChangeDate | date |  |  | SI | Date of Antenatal Care Change |
| PREG_CareChangeReason_DR | bigint |  | FK | SI | Des Ref PAC_AntenatalCareChangeReason |
| PREG_Chorionicity_DR | bigint |  | FK | SI | Chorionicity |
| PREG_Comments | varchar |  |  | SI | Comments |
| PREG_Confidential | varchar |  |  | SI | Confidentiality Flag |
| PREG_ConfidentialReason | varchar |  |  | SI | Confidential Reason |
| PREG_ConsDegree_DR | bigint |  | FK | SI | Des Ref ConsDegree |
| PREG_ConsangBetwParents_DR | bigint |  | FK | SI | Des Ref ORCConsanguinityBetweenParents |
| PREG_Consultant | varchar |  |  | SI | Consultant |
| PREG_ContactForename | varchar |  |  | SI | Pregnancy Contact Forename |
| PREG_ContactSurname | varchar |  |  | SI | Pregnancy Contact Surname |
| PREG_CoombsTest | varchar |  |  | SI | Coombs Test |
| PREG_CycleL | double |  |  | SI | CycleL |
| PREG_DateContrcptStop | date |  |  | SI | DateContrcptStop |
| PREG_DateOfBooking | date |  |  | SI | Date of Booking |
| PREG_DateRDSProphylaxis | date |  |  | SI | DateRDSProphylaxis |
| PREG_Daysofbleeding | double |  |  | SI | Daysofbleeding |
| PREG_DelivPlanManagement_DR | bigint |  | FK | SI | Des Ref PAC_DelivPlanManag |
| PREG_DiagnosisDate | date |  |  | SI | DiagnosisDate |
| PREG_DiagnosisDate1 | date |  |  | SI | DiagnosisDate1 |
| PREG_DiagnosisDate2 | date |  |  | SI | DiagnosisDate2 |
| PREG_DiagnosisDate3 | date |  |  | SI | DiagnosisDate3 |
| PREG_DiagnosisDate4 | date |  |  | SI | DiagnosisDate4 |
| PREG_DrugSupplDuringPregn | varchar |  |  | SI | Drug Supplement During Pregnancy |
| PREG_EDDDiffLMPAndLatestUS | double |  |  | SI | EDD Difference between LMP and Latest U/S (weeks) |
| PREG_EdcAgreed | date |  |  | SI | Agreed EDC |
| PREG_EdcLnmp | date |  |  | SI | Est. date of confinement based on LNMP |
| PREG_EdcUltrasound1 | date |  |  | SI | Est. date of confinement based on u/s |
| PREG_EdcUltrasound2 | date |  |  | SI | EDC by Ultrasound 2 |
| PREG_EdcUltrasound3 | date |  |  | SI | EDC by ultrasound 3 |
| PREG_EndedDate | date |  |  | SI | Ended Date of Completed or Canceled Pregnancy |
| PREG_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PREG_EstEDD | varchar |  |  | SI | EstEDD |
| PREG_Exploration | varchar |  |  | SI | Exploration |
| PREG_FatherBldType_DR | bigint |  | FK | SI | Des Ref FatherBldType |
| PREG_FatherCheckbox1 | varchar |  |  | SI | Father Checkbox1 |
| PREG_FatherCheckbox2 | varchar |  |  | SI | Father Checkbox2 |
| PREG_FatherCheckbox3 | varchar |  |  | SI | Father Checkbox3 |
| PREG_FatherCheckbox4 | varchar |  |  | SI | Father Checkbox4 |
| PREG_FatherCheckbox5 | varchar |  |  | SI | Father Checkbox5 |
| PREG_FatherChildrenTogether | double |  |  | SI | How many children together  |
| PREG_FatherContactType_DR | bigint |  | FK | SI | Des Ref PACContactType |
| PREG_FatherDOB | date |  |  | SI | Father's DOB |
| PREG_FatherDate1 | date |  |  | SI | Father Date1 |
| PREG_FatherDate2 | date |  |  | SI | Father Date2 |
| PREG_FatherDate3 | date |  |  | SI | Father Date3 |
| PREG_FatherDate4 | date |  |  | SI | Father Date4 |
| PREG_FatherDate5 | date |  |  | SI | Father Date5 |
| PREG_FatherDetails | varchar |  |  | SI | Father Details |
| PREG_FatherFirstName | varchar |  |  | SI | Father's First Name |
| PREG_FatherLivingTogether | varchar |  |  | SI | Living Together |
| PREG_FatherNextOfKin_DR | varchar |  | FK | SI | Des Ref PA_Nok |
| PREG_FatherRelationType_DR | bigint |  | FK | SI | Des Ref CT_Relation |
| PREG_FatherSecondName | varchar |  |  | SI | Father's Second Name |
| PREG_FatherSurname | varchar |  |  | SI | Father's Surname |
| PREG_FatherText1 | varchar |  |  | SI | Father Text1 |
| PREG_FatherText2 | varchar |  |  | SI | Father Text2 |
| PREG_FatherText3 | varchar |  |  | SI | Father Text3 |
| PREG_FatherText4 | varchar |  |  | SI | Father Text4 |
| PREG_FatherText5 | varchar |  |  | SI | Father Text5 |
| PREG_FeedIntention_DR | bigint |  | FK | SI | Des Ref PAC_FeedType |
| PREG_FetusThisPreg | bigint |  |  | SI | No. of fetus this Pregnancy |
| PREG_FirstPregnancy | varchar |  |  | SI | First Pregnancy |
| PREG_FoetusComplications | varchar |  |  | SI | FoetusComplications  |
| PREG_FreeText1 | varchar |  |  | SI | FreeText1 |
| PREG_GIRFECLeadProf | varchar |  |  | SI | GIRFEC lead professional if relevant |
| PREG_GPInformPreg | varchar |  |  | SI | GP informed of pregnancy  |
| PREG_GPInformedDate | date |  |  | SI | GP Informed date |
| PREG_GestationDaysUS1 | double |  |  | SI | Gestation Days for First Ultrasound |
| PREG_GestationDaysUS2 | double |  |  | SI | Gestation Days for Second Ultrasound |
| PREG_GestationDaysUS3 | double |  |  | SI | Gestation Days for Third Ultrasound |
| PREG_GestationWeeksUS1 | double |  |  | SI | Gestation Weeks for First Ultrasound |
| PREG_GestationWeeksUS2 | double |  |  | SI | Gestation Weeks for Second Ultrasound |
| PREG_GestationWeeksUS3 | double |  |  | SI | Gestation Weeks for Third Ultrasound |
| PREG_HistUterineAnomaly | varchar |  |  | SI | HistUterineAnomaly |
| PREG_Hospitalised | varchar |  |  | SI | Hospitalised |
| PREG_Hospitalised1 | varchar |  |  | SI | Hospitalised1 |
| PREG_Hospitalised2 | varchar |  |  | SI | Hospitalised2 |
| PREG_Hospitalised3 | varchar |  |  | SI | Hospitalised3 |
| PREG_Hospitalised4 | varchar |  |  | SI | Hospitalised4 |
| PREG_ID | varchar |  |  | SI | PregnancyID |
| PREG_IntendedDelivPlace_DR | bigint |  | FK | SI | Des Ref PAC_DeliveryPlace  |
| PREG_LabourMth_DR | bigint |  | FK | SI | Des Ref LabourMth |
| PREG_LatestUSDate | date |  |  | SI | Latest U/S Date |
| PREG_Leopold | varchar |  |  | SI | Leopold |
| PREG_LmpApproxDateFlag | varchar |  |  | SI | LMP approximate date flag |
| PREG_Lnmp | date |  |  | SI | Date of LNMP |
| PREG_LocalityTeamContact | varchar |  |  | SI | Midwife Locality Team Contact |
| PREG_Menarche | date |  |  | SI | Menarche |
| PREG_MenstCycleReg | varchar |  |  | SI | MenstCycleReg |
| PREG_MidCommTeam_DR | bigint |  | FK | SI | Midwife Community Team |
| PREG_MidwifeTeamBase | varchar |  |  | SI | Midwifery team base |
| PREG_NoOfUSForClinReasons | double |  |  | SI | No. of U/S for clinical reasons |
| PREG_NoOfUSForOtherReasons | double |  |  | SI | No. of U/S for other reasons |
| PREG_Notes | varchar |  |  | SI | Notes |
| PREG_Notes1 | varchar |  |  | SI | Notes1 |
| PREG_Notes2 | varchar |  |  | SI | Notes2 |
| PREG_Notes3 | varchar |  |  | SI | Notes3 |
| PREG_Notes4 | varchar |  |  | SI | Notes4 |
| PREG_Number1 | double |  |  | SI | Number1 |
| PREG_Number2 | double |  |  | SI | Number2 |
| PREG_OriginalBookingText | varchar |  |  | SI | Original Booking free text |
| PREG_OriginalBooking_DR | bigint |  | FK | SI | Des Ref PAC_OriginalBooking |
| PREG_OthAntenatalCompl | varchar |  |  | SI | Other Antenatal Complications |
| PREG_OthOper | varchar |  |  | SI | Other Operations |
| PREG_OthProc | varchar |  |  | SI | Other Procedures |
| PREG_OtherCareProvider | varchar |  |  | SI | Other Care Provider   |
| PREG_PatType_DR | bigint |  | FK | SI | Des Ref PACPatientType |
| PREG_PatholEvent1_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| PREG_PatholEvent2_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| PREG_PatholEvent3_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| PREG_PatholEvent4_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| PREG_PatholEvent_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| PREG_Person_DR | bigint |  | FK | SI | Des Ref Person |
| PREG_PostnatalCompl | varchar |  |  | SI | PostnatalCompl |
| PREG_PregCycle | varchar |  |  | SI | PregCycle text  |
| PREG_PregDaysBleeding | varchar |  |  | SI | PregDaysBleeding text  |
| PREG_PregType | varchar |  |  | SI | Pregnancy Type |
| PREG_PregnAtAnamnesticRisk | varchar |  |  | SI | Pregnancy at Anamnestic Risk |
| PREG_PregnAtAnamnesticRiskText | varchar |  |  | SI | Free Text Pregnancy at Anamnestic Risk |
| PREG_PregnAtCurrentRisk | varchar |  |  | SI | Pregnancy at Current Risk |
| PREG_PregnAtPhysioRisk | varchar |  |  | SI | Pregnancy at Physiological Risk |
| PREG_PregnAtPhysioRiskText | varchar |  |  | SI | Free Text Pregnancy at Physiological Risk |
| PREG_PrenatScreenOutcome | varchar |  |  | SI | Prenatal Screening Outcome |
| PREG_PrenatScreenTestDone | varchar |  |  | SI | Des Ref ORCPrenatalScreenTestsDone
Property PREGP... |
| PREG_PrenatalKaryotype | varchar |  |  | SI | Prenatal Karyotype |
| PREG_PrevAntiRh | date |  |  | SI | Date of previous anti-rh |
| PREG_RDSProphylaxis | varchar |  |  | SI | RDS Prophylaxis |
| PREG_RUC | varchar |  |  | SI | RUC |
| PREG_ReasonTypeAntenatalCare | varchar |  |  | SI | Reason for Type of Antenatal Care |
| PREG_Rhesus_DR | bigint |  | FK | SI | [DEPRECATED]Item moved to PACBloodType in TC-11273... |
| PREG_RubellaImmune_DR | bigint |  | FK | SI | Des ref PAC_RubellaImmune_Status |
| PREG_ScanGestCertainty_DR | bigint |  | FK | SI | Certainty of gestation based on Scan |
| PREG_Status | bigint |  |  | SI | Pregnancy Status |
| PREG_StatusBeforeError_DR | bigint |  | FK | SI | Des Ref Pregnancy Status Before Pregnancy Was Mark... |
| PREG_SupplemPregnancy_DR | bigint |  | FK | SI | Des Ref ORCSupplemduringPregnancy |
| PREG_Text1 | varchar |  |  | SI | Text1 |
| PREG_Text10 | varchar |  |  | SI | Text10 |
| PREG_Text2 | varchar |  |  | SI | Text2 |
| PREG_Text3 | varchar |  |  | SI | Text3 |
| PREG_Text4 | varchar |  |  | SI | Text4 |
| PREG_Text5 | varchar |  |  | SI | Text5 |
| PREG_Text6 | varchar |  |  | SI | Text6 |
| PREG_Text7 | varchar |  |  | SI | Text7 |
| PREG_Text8 | varchar |  |  | SI | Text8 |
| PREG_Text9 | varchar |  |  | SI | Text9 |
| PREG_TimeOfBooking | time |  |  | SI | Time of Booking |
| PREG_TransferredDelivery | bit |  |  | SI | Transferred Delivery |
| PREG_Treatment | varchar |  |  | SI | Treatment |
| PREG_Treatment1 | varchar |  |  | SI | Treatment1 |
| PREG_Treatment2 | varchar |  |  | SI | Treatment2 |
| PREG_Treatment3 | varchar |  |  | SI | Treatment3 |
| PREG_Treatment4 | varchar |  |  | SI | Treatment4 |
| PREG_US1Date | date |  |  | SI | Date of First Ultrasound |
| PREG_US2Date | date |  |  | SI | Date of Second Ultrasound |
| PREG_US3Date | date |  |  | SI | Date of Third Ultrasound |
| PREG_Ultrasounds1 | double |  |  | SI | No. of ultrasounds in 1st trimester |
| PREG_Ultrasounds2 | double |  |  | SI | No. of ultrasounds in 2nd trimester |
| PREG_Ultrasounds3 | double |  |  | SI | No. of ultrasounds in 3rd trimester |
| PREG_UpdateDate | date |  |  | SI | Last Update Date |
| PREG_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| PREG_UpdateTime | time |  |  | SI | Last Update Time |
| PREG_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| PREG_VaginalBirthPlan_DR | bigint |  | FK | SI | Des Ref PAC_VaginalBirthAfterCaesarean |
| PREG_WeekOf1stTrimesterUS | double |  |  | SI | Week of 1st Trimester U/S  |
| PREG_WeekOfFatalGrowthRestr | double |  |  | SI | WeekOfFatalGrowthRestriction (FRG) |
| PREG_WeekOfMorphologicUS | double |  |  | SI | Week of Morphologic U/S |
| PREG_YesNo1 | varchar |  |  | SI | YesNo1 |
| PREG_YesNo10 | varchar |  |  | SI | YesNo10 |
| PREG_YesNo11 | varchar |  |  | SI | YesNo11 |
| PREG_YesNo12 | varchar |  |  | SI | YesNo12 |
| PREG_YesNo13 | varchar |  |  | SI | YesNo13 |
| PREG_YesNo2 | varchar |  |  | SI | YesNo2 |
| PREG_YesNo3 | varchar |  |  | SI | YesNo3 |
| PREG_YesNo4 | varchar |  |  | SI | YesNo4 |
| PREG_YesNo5 | varchar |  |  | SI | YesNo5 |
| PREG_YesNo6 | varchar |  |  | SI | YesNo6 |
| PREG_YesNo7 | varchar |  |  | SI | YesNo7 |
| PREG_YesNo8 | varchar |  |  | SI | YesNo8 |
| PREG_YesNo9 | varchar |  |  | SI | YesNo9 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*