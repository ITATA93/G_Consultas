# SQLUser.INC_ItmRecIngr

**Schema:** SQLUser
**Columnas:** 202
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INRIN_ParRef | varchar | PK |  | NO | INC_ItmRcp Parent Reference |
| INRIN_AdhocItem | varchar |  |  | SI | Flag to indicate this is an auto-created stock ite... |
| INRIN_Childsub | double |  |  | NO | Childsub |
| INRIN_CreatedDate | date |  |  | SI | Created Date |
| INRIN_CreatedTime | time |  |  | SI | Created Time |
| INRIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INRIN_Date_Updated | date |  |  | SI | Date Updated |
| INRIN_INCI_DR | bigint |  | FK | NO | Des Ref to INCI |
| INRIN_Qty | double |  |  | NO | Qty Required |
| INRIN_Remarks | varchar |  |  | SI | Remarks |
| INRIN_RowId | varchar |  |  | NO | - |
| INRIN_Time_Updated | time |  |  | SI | Time Updated |
| INRIN_UOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| INRIN_UpdatedDate | date |  |  | SI | Updated Date |
| INRIN_UpdatedTime | time |  |  | SI | Updated Time |
| INRIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INRIN_User_Updated_DR | bigint |  | FK | SI | User Updated Des Ref to SSU |
| Q01 | - |  |  | SI | Before Induction of Anaesthesia |
| Q02 | - |  |  | SI | Sign in |
| Q03 | - |  |  | SI | Patient has confirmed |
| Q04 | - |  |  | SI | Identity |
| Q05 | - |  |  | SI | Site marked |
| Q06 | - |  |  | SI | Procedure |
| Q07 | - |  |  | SI | Consent |
| Q08 | - |  |  | SI | Site marked |
| Q09 | - |  |  | SI | Check equipamiento de anestesia completado |
| Q10 | - |  |  | SI | Pulse oximeter on patient and functioning |
| Q100 | - |  |  | SI | Present necessary consents |
| Q101 | - |  |  | SI | Anaesthesia Equipment Check Completed |
| Q102 | - |  |  | SI | Pulse oximeter and ECG on patient |
| Q103 | - |  |  | SI | Identification of known allergy risks |
| Q104 | - |  |  | SI | Difficulty in managing the airways or risk of aspi... |
| Q105 | - |  |  | SI | Limitations to the required position |
| Q106 | - |  |  | SI | The risk of blood loss was assessed (> 500ml or> 7... |
| Q107 | - |  |  | SI | Check team |
| Q108 | - |  |  | SI | Surgeon, anesthetist and nurses confirmed: the pat... |
| Q109 | - |  |  | SI | Has antibiotic prophylaxis been give within the la... |
| Q11 | - |  |  | SI | Essential equipment available |
| Q110 | - |  |  | SI | Statement by the surgeon on duration of surgery, r... |
| Q111 | - |  |  | SI | Statement by the anesthetist on patient specificit... |
| Q112 | - |  |  | SI | Verification by the nurse about the availability o... |
| Q113 | - |  |  | SI | Any essential radiological imaging available? |
| Q114 | - |  |  | SI | Confirm name of procedure performed |
| Q115 | - |  |  | SI | The final count of gauzes, scalpels, needles and o... |
| Q116 | - |  |  | SI | The specimen is labelled (including patient name) |
| Q117 | - |  |  | SI | Correct registration of the implanted prosthetic m... |
| Q118 | - |  |  | SI | The team reviewed the important and critical aspec... |
| Q119 | - |  |  | SI | Reporting any problems connected to the equipment |
| Q12 | - |  |  | SI | Does the patient have a known allergy? |
| Q120 | - |  |  | SI | The postoperative plan for DVT prophylaxis, antibi... |
| Q121 | - |  |  | SI | Equipment and prosthesis available |
| Q124 | - |  |  | SI | Identity |
| Q125 | - |  |  | SI | Site marked |
| Q126 | - |  |  | SI | Procedure |
| Q127 | - |  |  | SI | Consent |
| Q128 | - |  |  | SI | Pulse oximeter on patient and functioning |
| Q129 | - |  |  | SI | Confirm all team members have introduced themselve... |
| Q13 | - |  |  | SI | Does the patient have a known difficult airway or ... |
| Q130 | - |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q131 | - |  |  | SI | Correct patient |
| Q132 | - |  |  | SI | Correct site and side of procedure |
| Q133 | - |  |  | SI | Correct procedure |
| Q134 | - |  |  | SI | Nurse confirm with the team the name of the proced... |
| Q135 | - |  |  | SI | Surgeon, anaesthesia professional and nurse review... |
| Q136 | - |  |  | SI | That instrument, sponge and needle counts are corr... |
| Q137 | - |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q138 | - |  |  | SI | Anaesthesia team reviews: are there any patient - ... |
| Q139 | - |  |  | SI | Nursing team reviews: has sterility (including ind... |
| Q14 | - |  |  | SI | Does the patient have a known risk of >500ml blood... |
| Q140 | - |  |  | SI | Has the patient confirmed his/her identity, site, ... |
| Q141 | - |  |  | SI | Has the position of the patient at surgery been pr... |
| Q142 | - |  |  | SI | Does the patient have a known difficult airway or ... |
| Q143 | - |  |  | SI | Operation number |
| Q144 | - |  |  | SI | Operation / Procedure |
| Q145 | - |  |  | SI | Essential equipment available |
| Q15 | - |  |  | SI | Before skin incision |
| Q16 | - |  |  | SI | Time out |
| Q17 | - |  |  | SI | Confirm all team members have introduced themselve... |
| Q18 | - |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q19PROFESSIONAL | - |  |  | SI | Correct patient |
| Q20PROFESSIONAL | - |  |  | SI | Correct site and side of procedure |
| Q21PROFESSIONAL | - |  |  | SI | Correct procedure |
| Q22 | - |  |  | SI | Anticipated critical events |
| Q22a | - |  |  | SI | Anticipated critical events |
| Q23 | - |  |  | SI | Has antibiotic prophylaxis been give within the la... |
| Q24 | - |  |  | SI | Is essential imaging displayed? |
| Q25 | - |  |  | SI | Before patient leaves operation room |
| Q26 | - |  |  | SI | Sign out |
| Q27 | - |  |  | SI | Nurse verbally confirms with the team |
| Q28 | - |  |  | SI | Nurse confirm with the team the name of the proced... |
| Q29 | - |  |  | SI | Completion of instrument, sponge and needle counts |
| Q30 | - |  |  | SI | Specimen labelling (read specimen labels aloud, in... |
| Q31 | - |  |  | SI | Whether There Are Any Equipament Problems To Be Ad... |
| Q32 | - |  |  | SI | Surgeon, anaesthesia professional and nurse review... |
| Q33 | - |  |  | SI | Nurse verbally confirms with the team |
| Q34 | - |  |  | SI | That instrument, sponge and needle counts are corr... |
| Q35 | - |  |  | SI | Sign in time |
| Q36 | - |  |  | SI | Time out time |
| Q37 | - |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q38 | - |  |  | SI | Are there equipment issues or any concerns |
| Q39 | - |  |  | SI | Sign out time |
| Q40 | - |  |  | SI | Anaesthesia team reviews: are there any patient-sp... |
| Q41 | - |  |  | SI | Nursing Team Reviews: Has Sterility (Including Ind... |
| Q42 | - |  |  | SI | Any essential radiological imaging available? |
| Q43 | - |  |  | SI | All surgical equipment & prosthesis checked and av... |
| Q44 | - |  |  | SI | Any known alerts? |
| Q45 | - |  |  | SI | Blood availability? |
| Q45a | - |  |  | SI | Blood availability? |
| Q46 | - |  |  | SI | Sign in completed by |
| Q47 | - |  |  | SI | Sign in time |
| Q48 | - |  |  | SI | Sign in date |
| Q49 | - |  |  | SI | Sign in complete |
| Q50 | - |  |  | SI | Patient positioned correctly and safely |
| Q51 | - |  |  | SI | All essential monitoring applied and functioning |
| Q52 | - |  |  | SI | Venous thromboprophylaxis? |
| Q53 | - |  |  | SI | Sterility confirmed |
| Q54 | - |  |  | SI | Equipment and prosthesis available |
| Q55 | - |  |  | SI | Critical events / Concerns notes |
| Q56 | - |  |  | SI | Time out completed by |
| Q57 | - |  |  | SI | Time out time |
| Q58 | - |  |  | SI | Time out date |
| Q59 | - |  |  | SI | Time out complete |
| Q60 | - |  |  | SI | Any radiological imaging, personal effects and any... |
| Q61 | - |  |  | SI | Comments |
| Q62 | - |  |  | SI | Sign out completed by |
| Q63 | - |  |  | SI | Sign out time |
| Q64 | - |  |  | SI | Sign out date |
| Q65 | - |  |  | SI | Sign out complete |
| Q66 | - |  |  | SI | The instrument, sponge and sharps are correct? |
| Q67 | - |  |  | SI | The specimen is labelled (including patient name) |
| Q68 | - |  |  | SI | Whether there are any equipment problems to be add... |
| Q69 | - |  |  | SI | Pre anaesthesia assessment |
| Q70 | - |  |  | SI | In case under LA procedure |
| Q71 | - |  |  | SI | Antibiotic prophylaxis with 60 - 120 min. before i... |
| Q72 | - |  |  | SI | Time administered |
| Q73 | - |  |  | SI | Sterilization indicators have been confirmed |
| Q74 | - |  |  | SI | Surgical fire risk assessment |
| Q75 | - |  |  | SI | Notes |
| Q76 | - |  |  | SI | Second care provider signature |
| Q77 | - |  |  | SI | Has the patient confirmed his/her identity, site, ... |
| Q78 | - |  |  | SI | Post - operative bed booked |
| Q79 | - |  |  | SI | Surgeon reviews: what are the critical or unexpect... |
| Q80 | - |  |  | SI | Anaesthesia team reviews: are there any patient-sp... |
| Q81 | - |  |  | SI | Nursing team reviews: has sterility (including ind... |
| Q82 | - |  |  | SI | Venous thromboprophylaxis? |
| Q83 | - |  |  | SI | Sign in surgeon |
| Q84 | - |  |  | SI | Sign in anaesthetist |
| Q85 | - |  |  | SI | To be completed with at least nurse, anaesthetist ... |
| Q86 | - |  |  | SI | Surgeon, anaesthesia professional and nurse verbal... |
| Q87 | - |  |  | SI | Has antibiotic prophylaxis been given within the l... |
| Q88 | - |  |  | SI | Time out surgeon |
| Q89 | - |  |  | SI | Time out anaesthetist |
| Q90 | - |  |  | SI | To be completed with at least nurse, anaesthetist ... |
| Q91 | - |  |  | SI | Sign out surgeon |
| Q92 | - |  |  | SI | Sign out anaesthetist |
| Q93 | - |  |  | SI | To be completed with at least nurse and anaestheti... |
| Q94 | - |  |  | SI | Nurse confirms verbally with the team |
| Q95 | - |  |  | SI | Date |
| Q96 | - |  |  | SI | Time |
| Q97 | - |  |  | SI | Anticipated critical events |
| Q98 | - |  |  | SI | Patient has confirmed |
| Q99 | - |  |  | SI | The patient confirmed: identity, surgery site, sur... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*