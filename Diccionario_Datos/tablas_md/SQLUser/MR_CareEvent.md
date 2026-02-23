# SQLUser.MR_CareEvent

**Schema:** SQLUser
**Columnas:** 189
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAREVT_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| CAREVT_Childsub | double |  |  | NO | Childsub |
| CAREVT_CustomText1 | varchar |  |  | SI | Custom Text Field 1 |
| CAREVT_Date | date |  |  | SI | Date |
| CAREVT_EndDate | date |  |  | SI | End Date |
| CAREVT_EndTime | time |  |  | SI | End Time |
| CAREVT_EnteredLoc_DR | bigint |  | FK | SI | Entered Location |
| CAREVT_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| CAREVT_ErrorReason_DR | bigint |  | FK | SI | Des Ref - Error Reason |
| CAREVT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CAREVT_Notes | varchar |  |  | SI | Notes |
| CAREVT_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| CAREVT_RowId | varchar |  |  | NO | - |
| CAREVT_Severity | varchar |  |  | SI | event severity |
| CAREVT_Time | time |  |  | SI | Time |
| CAREVT_Type_DR | bigint |  | FK | SI | Des Ref MRCCareEventType |
| CAREVT_UpdateDate | date |  |  | SI | UpdateDate |
| CAREVT_UpdateTime | time |  |  | SI | UpdateTime |
| CAREVT_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Fecha ingreso |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Información entregada por |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Anamnesis |
| Q07 | - |  |  | SI | Menarca |
| Q08 | - |  |  | SI | Acciones preventivas |
| Q09 | - |  |  | SI | Condición funcional básica |
| Q10 | - |  |  | SI | Red de Salud, conctato habitual |
| Q100 | - |  |  | SI | Texto especial, imagen y foto |
| Q100TxtOnly | - |  |  | SI | Texto especial, imagen y foto Plain Text Only |
| Q101 | - |  |  | SI | Útero de forma, tamano, consistencia y mobilidad n... |
| Q102 | - |  |  | SI | Útero de mobilidad moderadamiente dolorosa |
| Q103 | - |  |  | SI | Útero de mobilidad extremadamiente dolorosa |
| Q104 | - |  |  | SI | Útero aumentado de volumen pero dentro de los limi... |
| Q105 | - |  |  | SI | Massa o empastamiento anexial |
| Q106 | - |  |  | SI | FUR operativa |
| Q107 | - |  |  | SI | Criterio elejido para la FUR |
| Q108 | - |  |  | SI | Crecimiento uterino y edad gestacional |
| Q109 | - |  |  | SI | Circunferencia abdominal fetal ecografica |
| Q11 | - |  |  | SI | Condiciones familiares o sociales |
| Q110 | - |  |  | SI | Ecodoppler |
| Q111 | - |  |  | SI | Volumen de líquido amniótico |
| Q112 | - |  |  | SI | Feto reactivo en cardiotocografia, con FCF normal |
| Q113 | - |  |  | SI | Examen obstétrico |
| Q114 | - |  |  | SI | Observaciones |
| Q115 | - |  |  | SI | Residuo vaginal |
| Q116 | - |  |  | SI | label |
| Q117 | - |  |  | SI | Ciclos |
| Q118 | - |  |  | SI | Periodo |
| Q119 | - |  |  | SI | Fertilidad |
| Q12 | - |  |  | SI | Nutrición |
| Q120 | - |  |  | SI | Partos |
| Q121 | - |  |  | SI | Temperatura |
| Q121ObsDR | - |  |  | SI | Temperatura DR |
| Q122 | - |  |  | SI | Talla |
| Q122ObsDR | - |  |  | SI | Talla DR |
| Q124 | - |  |  | SI | Saturación oxígeno SPO2 |
| Q124ObsDR | - |  |  | SI | Saturación oxígeno SPO2 DR |
| Q125 | - |  |  | SI | Frecuencia cardiaca |
| Q125ObsDR | - |  |  | SI | Frecuencia cardiaca DR |
| Q126 | - |  |  | SI | Frecuencia respiratoria |
| Q126ObsDR | - |  |  | SI | Frecuencia respiratoria DR |
| Q13 | - |  |  | SI | Pérdida reciente de peso |
| Q14 | - |  |  | SI | Evaluación de Historia Ginecológica |
| Q15 | - |  |  | SI | Medicamentos de uso frequente o habitual |
| Q16 | - |  |  | SI | Evaluación y chequeo de antecedentes |
| Q17 | - |  |  | SI | Exame fisico general |
| Q18 | - |  |  | SI | Actitud |
| Q19 | - |  |  | SI | Disnea |
| Q20 | - |  |  | SI | Fiebre |
| Q21 | - |  |  | SI | Palidez |
| Q22 | - |  |  | SI | Ictericia |
| Q23 | - |  |  | SI | Lista neurológica |
| Q25 | - |  |  | SI | Examen neurológico |
| Q26 | - |  |  | SI | Marcha y equilibrio normales |
| Q27 | - |  |  | SI | Region inguinal |
| Q28 | - |  |  | SI | Vulva |
| Q29 | - |  |  | SI | Perineo |
| Q30 | - |  |  | SI | Condicón funcional específica |
| Q31 | - |  |  | SI | Lista especialidad |
| Q32 | - |  |  | SI | Reflexos normales |
| Q33 | - |  |  | SI | Reflexos patelares exaltados |
| Q34 | - |  |  | SI | Perinatal |
| Q35 | - |  |  | SI | Biópsias |
| Q36 | - |  |  | SI | Cirurgias |
| Q37 | - |  |  | SI | Deformaciones anatómicas importantes por |
| Q38 | - |  |  | SI | Menopausa |
| Q39 | - |  |  | SI | Vagina con complacencia y elasticidad normales |
| Q40 | - |  |  | SI | Lista de locales |
| Q41 | - |  |  | SI | Sustentación uterovaginal |
| Q42 | - |  |  | SI | Evaluación especialidad |
| Q43 | - |  |  | SI | Membros inferiores |
| Q44 | - |  |  | SI | Lista antecedentes generales |
| Q45 | - |  |  | SI | Examen ginecológico |
| Q46 | - |  |  | SI | Cuello uterino de tamano normal |
| Q47 | - |  |  | SI | Cuello uterino hipertrófico |
| Q48 | - |  |  | SI | Colposcopia sin alteraciones displásicas de color,... |
| Q49 | - |  |  | SI | Colposcopia con alteraciones displásicas de relevo... |
| Q50 | - |  |  | SI | Colposcopia con alteraciones displásicas de color,... |
| Q51 | - |  |  | SI | Lista cara y cuello |
| Q52 | - |  |  | SI | Examen nariz, boca y cuello |
| Q53 | - |  |  | SI | Dentición completa |
| Q54 | - |  |  | SI | Dientes en buen estado |
| Q55 | - |  |  | SI | Dientes en malo estado |
| Q56 | - |  |  | SI | Orofaringe normal |
| Q57 | - |  |  | SI | Orofaringe hiperémica |
| Q58 | - |  |  | SI | Blumberg |
| Q59 | - |  |  | SI | Lista pulmonar |
| Q60 | - |  |  | SI | Examen pulmonar |
| Q61 | - |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | - |  |  | SI | Taquipneico |
| Q63 | - |  |  | SI | Dispneico |
| Q64 | - |  |  | SI | Roncos |
| Q65 | - |  |  | SI | Sibilos en espiración |
| Q66 | - |  |  | SI | Lista cardíaca |
| Q67 | - |  |  | SI | Examen cardíaco |
| Q68 | - |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | - |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | - |  |  | SI | Taquicardia |
| Q71 | - |  |  | SI | Lista abdominal |
| Q72 | - |  |  | SI | Examen abdominal |
| Q73 | - |  |  | SI | Abdome depresible, sin resistencia a la palpación ... |
| Q74 | - |  |  | SI | Ausencia de viceromegalias o masas palpables |
| Q75 | - |  |  | SI | Lista ginecológica completa |
| Q76 | - |  |  | SI | Utero aumentado de volumen proyectandose hacia fue... |
| Q77 | - |  |  | SI | Exame mamas |
| Q78 | - |  |  | SI | Lista extremidades |
| Q79 | - |  |  | SI | Exame extremidades |
| Q80 | - |  |  | SI | Conclusion |
| Q81 | - |  |  | SI | Contacto preventivo sin allajos importantes |
| Q82 | - |  |  | SI | Gestación de evolución normal, con bajo riesgo |
| Q83 | - |  |  | SI | Enbarazo de alto riesgo con acompanhamiente obstét... |
| Q84 | - |  |  | SI | Condicion aguda o nueva para el paciente |
| Q85 | - |  |  | SI | Riesgo de prematuirdad en condiciones de GES |
| Q86 | - |  |  | SI | Plan |
| Q87 | - |  |  | SI | Notificar atendimiento a garantia GES |
| Q88 | - |  |  | SI | Notificar nueva garantia GES |
| Q89 | - |  |  | SI | Solicitar examenes de laboratorio |
| Q90 | - |  |  | SI | Solicitar examenes de imagen |
| Q91 | - |  |  | SI | Solicitar examen anatomopatologico |
| Q92 | - |  |  | SI | Periodo de observacion de la evolucion en la unida... |
| Q93 | - |  |  | SI | Hospitalizacion |
| Q94 | - |  |  | SI | Solicitar parecer especializado |
| Q95 | - |  |  | SI | Retorno programado |
| Q96 | - |  |  | SI | Examenes laboratorio |
| Q97 | - |  |  | SI | Examenes Imagenes |
| Q98 | - |  |  | SI | Examenes histopatologicos |
| Q99 | - |  |  | SI | imagen |
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