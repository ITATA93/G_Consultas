# Tools_DrugUpload.OptionsImport

**Schema:** Tools_DrugUpload
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TDUOI_RowId | bigint | PK |  | NO | - |
| AdRe | varchar |  |  | SI | Part 1 Refresh: Y = AdminRoute-Links for DrgForms ... |
| Admi | varchar |  |  | SI | Import Default: Admin Route |
| BCod | varchar |  |  | SI | Append Code to Brand |
| CCAu | varchar |  |  | SI | CCR & Audit OFF |
| ChnE | varchar |  |  | SI | Change End dated Drugs |
| Clea | varchar |  |  | SI | post upload clean
0= no cleanup 
or comma separa... |
| CpyI | varchar |  |  | SI | Copy Instructions from DrgForm to RtFrm |
| DPa2 | varchar |  |  | SI | [Y/N],[Y/N] = Force single DrgForm, DrgPack 
DrgF... |
| DPac | varchar |  |  | SI | DrugForm Pack Generation Options (derive has only ... |
| DRtA | varchar |  |  | SI | DrugForm AdminRoute CopyfromCT, CopyMissing 
(COP... |
| Deci | varchar |  |  | SI | Decimal symbols used in Files Europe:., 1.000,12 U... |
| Dele | integer |  |  | SI | PRE Upload Cleanup Drugs Level 
0 = no cleanup 
... |
| Disp | varchar |  |  | SI | Import Default: Dispensing Time |
| DoRe | varchar |  |  | SI | Refresh Dose Equivalents |
| Dtcm | integer |  |  | SI | Import Default: Dupl Therapy Num Allows |
| DupA | bit |  |  | SI | Flags for update duplicate entries
On UI check bo... |
| DupD | bit |  |  | SI | D=FormDoseEquiv,  |
| DupI | bit |  |  | SI | I=DrgFormInstructions |
| DupO | bit |  |  | SI | O = DrgFormOther |
| DupPO | bit |  |  | SI | PO = DrgFormPackOther |
| Dura | varchar |  |  | SI | Import Default: Duration |
| Duri | varchar |  |  | SI | Import Default: InPat Duration |
| EMFr | varchar |  |  | SI | External Mono From Path |
| EMTo | varchar |  |  | SI | External Mono To Path  |
| EqRe | varchar |  |  | SI | Refresh Equivalence Groups |
| ExRe | varchar |  |  | SI | Clean References pre-upload
0= no cleanup 
1= de... |
| ExtCodUp | integer |  |  | SI | Update logic for handling of order item external c... |
| FPFrly | varchar |  |  | SI | Respect Function Preferences for Formulary items Y... |
| FPNFrly | varchar |  |  | SI | Respect Function Preferences for NON Formulary ite... |
| FiEn | varchar |  |  | SI | File Encoding: Force FileEncoding if files do not ... |
| Form | varchar |  |  | SI | Import Default: Form |
| Freq | varchar |  |  | SI | Import Default: Frequency |
| Frly | varchar |  |  | SI | Import Default: Formulary |
| FrmC | varchar |  |  | SI | DrugForm code rule:
Format: [Type],[delimiter],[P... |
| FrmD | varchar |  |  | SI | Drug Form Description as a combination of 
[Brand... |
| GCAl | varchar |  |  | SI | Add Generic Code as Alias |
| GCod | varchar |  |  | SI | Append Code to Generic |
| GLab | varchar |  |  | SI | Generic Description to Label |
| Gene | varchar |  |  | SI | Import Default: Generic |
| GfTc | varchar |  |  | SI | Generic Rt Form or Generic Based |
| ImpE | varchar |  |  | SI | Import Enddated / EndDate Equiv |
| InRe | varchar |  |  | SI | Refresh Interactions
Y/N and second Parameter = D... |
| Inst | varchar |  |  | SI | Import Default: Instruction |
| Logf | integer |  |  | SI | Log Filter Level |
| NBfN | varchar |  |  | SI | Set Do not allow prescribing in BaseUOM to No when... |
| PacEndD | bit |  |  | SI | Import NEW DrgFormPack as enddated ALWAYS |
| Pack | varchar |  |  | SI | Import Default: Pack Size (PHC) |
| Path | varchar |  |  | SI | Import "Settings/Options"
Path where Import Files... |
| PckC | varchar |  |  | SI | Drug Form Pack Code  Format: [Type],[Delimiter] 
... |
| PckD | varchar |  |  | SI | Prepend to Drug Form Pack Description a combinatio... |
| PnRe | varchar |  |  | SI | Refresh Prescription Notes aka AIFA |
| Pois | varchar |  |  | SI | Import Default: Controlled Drug Cat |
| PrAdUp | integer |  |  | SI | Update Logic DrgForm-AdminRoute |
| PrCaUp | integer |  |  | SI | Update Logic DrgMast Categories |
| PrExUp | integer |  |  | SI | Update Logic DrgForm-Extra Details |
| PrFoUp | integer |  |  | SI | Update Logic DrgForm - Form |
| PrFyUp | integer |  |  | SI | Update Logic DrgForm/Pack Formulary |
| PrGeUp | integer |  |  | SI | Update Logic DrgForm/Mast Generic |
| PrInUp | integer |  |  | SI | Update Logic DrgForm-Instruction |
| PrL1Up | integer |  |  | SI | Update Logic DrgMast-Label 1  |
| PrL2Up | integer |  |  | SI | Update Logic DrgMast Label 2 |
| PrPaUp | integer |  |  | SI | Update Logic DrgForm/Pack-Pack |
| PrReUp | integer |  |  | SI | Update Logic DrgForm-MaxRep |
| PrRoUp | integer |  |  | SI | Update Logic DrgForm-Route |
| PrStUp | integer |  |  | SI | Update Logic DrgForm-Strength |
| PrUoUp | integer |  |  | SI | Update Logic DrgForm-BaseUOM |
| PrVoUp | integer |  |  | SI | Update Logic DrgForm-Volume |
| PreCUp | integer |  |  | SI | Update Logic Pregnancy Category (CT) |
| QaVo | varchar |  |  | SI | DoseEquiv - ML / L as Volume |
| Qadd | varchar |  |  | SI | DoseEquiv - Qty as Default Dose |
| Qivd | varchar |  |  | SI | DoseEquiv - Ignore Vendor Dose (Y=ignore value fro... |
| RegConfUpload | varchar |  |  | SI | - |
| RegPostUpload | varchar |  |  | SI | - |
| RegPreUpload | varchar |  |  | SI | Regional or Site Specific routines to be called
w... |
| Rout | varchar |  |  | SI | Import Default: Route |
| RpRe | varchar |  |  | SI | Refresh Repeatability |
| RtAd | integer |  |  | SI | Route/Admin Routes (CodeTable) 
(has only effect,... |
| SDCH | varchar |  |  | SI | SDC/OTC[,id]  SDC = link as Scheduled DrugClass fr... |
| StrUS | varchar |  |  | SI | Compare Strength as "UPPER and stripped spaces" 
... |
| Stre | varchar |  |  | SI | Import Default: Strength |
| StreUp | integer |  |  | SI | Update Logic Strength (CT) |
| SubC | varchar |  |  | SI | Import Default: Category & Sub Category |
| Uniq | varchar |  |  | SI | Append on Brand or Replace Code in Brand with a co... |
| Unit | varchar |  |  | SI | Import Default: Unit of Measure |
| UoRe | varchar |  |  | SI | Refresh UOM |
| UofMUp | integer |  |  | SI | Update Logic UOM (CT) |
| UpdateDate | date |  |  | SI | Last Update Date |
| UpdateTime | time |  |  | SI | Last Update Time |
| UpdateUserDR | bigint |  | FK | SI | Last Update User |
| UsSG | varchar |  |  | SI | For Schema Uploads: Name for the "unspecified subg... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*