# SQLUser.MRC_ClinPathwaysEpisodes

**Schema:** SQLUser
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EP_ParRef | bigint | PK |  | NO | MRC_ClinicalPathways Parent Reference |
| CQ106 | - |  |  | SI | (null) |
| CQ109 | - |  |  | SI | (null) |
| CQMC | - |  |  | SI | (null) |
| CQRDA | - |  |  | SI | (null) |
| CQROV | - |  |  | SI | (null) |
| EP_Childsub | double |  |  | NO | Childsub |
| EP_CreatedDate | date |  |  | SI | Created Date |
| EP_CreatedTime | time |  |  | SI | Created Time |
| EP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EP_CycleOffsetDays | double |  |  | SI | CycleOffsetDays |
| EP_Desc | varchar |  |  | SI | Description |
| EP_Episode | double |  |  | SI | Episode |
| EP_IPEpisodeRequired | varchar |  |  | SI | IP Episode Required |
| EP_RowId | varchar |  |  | NO | - |
| EP_TotalDays | double |  |  | SI | TotalDays |
| EP_UpdatedDate | date |  |  | SI | Updated Date |
| EP_UpdatedTime | time |  |  | SI | Updated Time |
| EP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | (c) Traslada agua de un vaso a otro sin derramar (... |
| Q10 | - |  |  | SI | (c) Copia una cruz (lám.1 lápiz |
| Q100 | - |  |  | SI | (M) Salta en un pie tres o más veces sin apoyo |
| Q101 | - |  |  | SI | (M) Coge una pelota (pelota) |
| Q102 | - |  |  | SI | (M) Camina hacia delante topando talón y punta |
| Q103 | - |  |  | SI | (M) Camina hacia atrás topando punta y talón. |
| Q104 | - |  |  | SI | Puntaje bruto |
| Q105 | - |  |  | SI | Puntaje T |
| Q106 | - |  |  | SI | Categoría |
| Q107 | - |  |  | SI | Puntaje bruto |
| Q108 | - |  |  | SI | Puntaje T |
| Q109 | - |  |  | SI | Categoria |
| Q11 | - |  |  | SI | (c) Copia un triángulo (lám.3 lápiz |
| Q110 | - |  |  | SI | Resultado TEPSI |
| Q110ObsDR | - |  |  | SI | Resultado TEPSI DR |
| Q12 | - |  |  | SI | (c) Copia un Cuadrado (lám.5 lápiz |
| Q13 | - |  |  | SI | (c)  Dibuja 9 o más partes de una figura humana (l... |
| Q14 | - |  |  | SI | (c) Dibuja 6 o más partes de una figura humana (lá... |
| Q15 | - |  |  | SI | (c) Dibuja 3 o más partes de una figura humana (lá... |
| Q16 | - |  |  | SI | (c) Ordena por tamaño (tablero |
| Q17 | - |  |  | SI | Chico |
| Q18 | - |  |  | SI | Grande |
| Q19 | - |  |  | SI | (L) Reconoce grande y chico (lám 6) |
| Q2 | - |  |  | SI | (c) Construye un puente con tres cubos con modelo ... |
| Q20 | - |  |  | SI | (L) Reconoce más y menos (lám 7) |
| Q21 | - |  |  | SI | Más |
| Q22 | - |  |  | SI | Menos |
| Q23 | - |  |  | SI | (L) Nombra animales (lám 8) |
| Q24 | - |  |  | SI | Gato |
| Q25 | - |  |  | SI | Perro |
| Q26 | - |  |  | SI | Chanchos |
| Q27 | - |  |  | SI | Patos |
| Q28 | - |  |  | SI | Paloma |
| Q29 | - |  |  | SI | Ovejas |
| Q3 | - |  |  | SI | (c) Contruye una torre de 8 o más cubos (doce cubo... |
| Q30 | - |  |  | SI | Tortuga |
| Q31 | - |  |  | SI | Gallina |
| Q32 | - |  |  | SI | (L) Nombra objetos (lám 5) |
| Q33 | - |  |  | SI | Vela |
| Q34 | - |  |  | SI | Escoba |
| Q35 | - |  |  | SI | Lápiz |
| Q36 | - |  |  | SI | Cama |
| Q37 | - |  |  | SI | Tijera |
| Q38 | - |  |  | SI | Jabón |
| Q39 | - |  |  | SI | (L) Discrimina pesado y liviano (bolsas con arena ... |
| Q4 | - |  |  | SI | (c) Desabotona (estuhe) |
| Q40 | - |  |  | SI | Pesado |
| Q41 | - |  |  | SI | Liviano |
| Q42 | - |  |  | SI | (L) Verbaliza su nombre y apellido |
| Q43 | - |  |  | SI | Apellido |
| Q44 | - |  |  | SI | Nombre |
| Q45 | - |  |  | SI | (L) Identifica su sexo |
| Q46 | - |  |  | SI | (L)Conoce el Nombre de sus padres |
| Q47 | - |  |  | SI | Madre |
| Q48 | - |  |  | SI | Padre |
| Q49 | - |  |  | SI | (L) Da respuestas coherentes a situaciones plantea... |
| Q5 | - |  |  | SI | (c) Abotona (estuche) |
| Q50 | - |  |  | SI | Cansado |
| Q51 | - |  |  | SI | Frío |
| Q52 | - |  |  | SI | Hambre |
| Q53 | - |  |  | SI | (L) Comprende preposiciones (lápiz) |
| Q54 | - |  |  | SI | Bajo |
| Q55 | - |  |  | SI | Detras |
| Q56 | - |  |  | SI | Sobre |
| Q57 | - |  |  | SI | (L) Razona por analogías opuestas |
| Q58 | - |  |  | SI | Hielo |
| Q59 | - |  |  | SI | Ratón |
| Q6 | - |  |  | SI | (c) Enhebra una aguja (aguja de lana, hilo) |
| Q60 | - |  |  | SI | Mamá |
| Q61 | - |  |  | SI | (L) Nombra colores (papel lustre) |
| Q62 | - |  |  | SI | Amarillo |
| Q63 | - |  |  | SI | Azul |
| Q64 | - |  |  | SI | Rojo |
| Q65 | - |  |  | SI | (L) Señala colores (papel lustre) |
| Q66 | - |  |  | SI | Amarillo |
| Q67 | - |  |  | SI | Azul |
| Q68 | - |  |  | SI | Rojo |
| Q69 | - |  |  | SI | (L) Nombra figuras geométricas |
| Q7 | - |  |  | SI | (c) Desata cordones (tablero c/ cordón) |
| Q70 | - |  |  | SI | Circulo |
| Q71 | - |  |  | SI | Cuadrado |
| Q72 | - |  |  | SI | Triangulo |
| Q73 | - |  |  | SI | (L) señala figuras geométricas (lám 12) |
| Q74 | - |  |  | SI | Circulo |
| Q75 | - |  |  | SI | Cuadrado |
| Q76 | - |  |  | SI | Triangulo |
| Q77 | - |  |  | SI | (L)Describe escenas (lám 13 y 14) |
| Q78 | - |  |  | SI | Lámina 13 |
| Q79 | - |  |  | SI | Lámina 14 |
| Q8 | - |  |  | SI | (c) Copia una línea recta (lám.1: lápiz |
| Q80 | - |  |  | SI | (L) Reconoce antes y después  (lám 17) |
| Q81 | - |  |  | SI | Antes |
| Q82 | - |  |  | SI | Después |
| Q83 | - |  |  | SI | (L) Define palabras |
| Q84 | - |  |  | SI | Manzana |
| Q85 | - |  |  | SI | Pelota |
| Q86 | - |  |  | SI | Zapato |
| Q87 | - |  |  | SI | Abrigo |
| Q88 | - |  |  | SI | (L)Nombra características de objeto |
| Q89 | - |  |  | SI | Pelota |
| Q9 | - |  |  | SI | (c) Copia un circulo (lám. 2 lápiz |
| Q90 | - |  |  | SI | Globo inflado |
| Q91 | - |  |  | SI | bolsa |
| Q92 | - |  |  | SI | (M) Salta con los dos pues juntos en el mismo luga... |
| Q93 | - |  |  | SI | (M) Camina diez pasos llevando un vaso lleno de ag... |
| Q94 | - |  |  | SI | (M) Lanza una pelota en una dirección determinada ... |
| Q95 | - |  |  | SI | (M) Se para en un pie sin apoyo 10 segundos o más |
| Q96 | - |  |  | SI | (M) Se para en un pie sin apoyo 05 segundos o más |
| Q97 | - |  |  | SI | (M) Se para en un pie 01 segundo o más |
| Q98 | - |  |  | SI | (M) Camina en punta de pies seis o más pasos |
| Q99 | - |  |  | SI | (M) Salta 20 cms. con los pies juntos (hoja reg.) |
| QACTEV | - |  |  | SI | Esta evaluación corresponde a: |
| QCUO | - |  |  | SI | (L) Conoce utilidad de objetos |
| QCUOa | - |  |  | SI | Cuchara |
| QCUOb | - |  |  | SI | Escoba |
| QMC | - |  |  | SI | Categoría |
| QMPB | - |  |  | SI | Puntaje bruto |
| QMPT | - |  |  | SI | Puntaje T |
| QNO5 | - |  |  | SI | Paraguas |
| QNO5b | - |  |  | SI | Tetera |
| QNO5c | - |  |  | SI | Zapatos |
| QNO5d | - |  |  | SI | Reloj |
| QNO5e | - |  |  | SI | Serrucho |
| QNO5f | - |  |  | SI | Taza |
| QOVC | - |  |  | SI | Comentarios |
| QRA | - |  |  | SI | (L) Reconoce Absurdo (lám. 15) |
| QRDA | - |  |  | SI | Resultado del desarrollo por Area |
| QRLCa | - |  |  | SI | Corto |
| QRLCb | - |  |  | SI | Largo |
| QRLCl | - |  |  | SI | (L) Reconoce largo y corto (lám. 1) |
| QROV | - |  |  | SI | Otra Vulnerabilidad |
| QRTTPB | - |  |  | SI | Puntaje Bruto |
| QRTTPT | - |  |  | SI | Puntaje T |
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
| QUP | - |  |  | SI | (L)Usa Plurales (lám. 16) |
| QVAa | - |  |  | SI | Cortado |
| QVAb | - |  |  | SI | Saltado |
| QVAc | - |  |  | SI | Planchado |
| QVAd | - |  |  | SI | Comiendo |
| QVAl | - |  |  | SI | (L) Verbaliza acciones (lám. 11) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*