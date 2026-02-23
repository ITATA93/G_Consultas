# Tools_DrugUpload.OptionsGeneration

**Schema:** Tools_DrugUpload
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TDUOG_RowId | bigint | PK |  | NO | - |
| Adro | varchar |  |  | SI | Order Desc Append
Append Route and/or Form and/or... |
| AlDe | varchar |  |  | SI | Alternative Description filled with
- 1 Official ... |
| AuCC | varchar |  |  | SI | Disable Audit and ChangeControl(Y,N) |
| Bgrp | varchar |  |  | SI | Derived / Default Billing Group
Format: Type,code... |
| Bsub | varchar |  |  | SI | Derived / Default Billing Sub Group
Format: Type,... |
| Dloc | varchar |  |  | SI | Stock Dispensing Location(s) 
Code1,Max;Code2,Max... |
| DmdB | varchar |  |  | SI | Billing Group for DMD Items |
| DmdC | varchar |  |  | SI | DMD Configuration Level:Generation (0=no, 1=yes, 2... |
| DmdO | varchar |  |  | SI | Order Categroy for DMD Items |
| DmdP | varchar |  |  | SI | DMD Level Prefix Level:Prefix
if Prefix is empty ... |
| DmdS | varchar |  |  | SI | Billing Sub Group for DMD Items |
| Eord | varchar |  |  | SI | EndDate Order for EndDated Drugs Y/N |
| Flag | varchar |  |  | SI | Stock
1) Gen StockItems for ALL,Formulary or NonF... |
| OCAl | varchar |  |  | SI | Add Order Item Code as Alias - used for all Levels... |
| OCGr | varchar |  |  | SI | Order Category Group 
Format: Code,Desc (for no G... |
| OFil | varchar |  |  | SI | Generation Filter 
(applies to Order & Stock) A o... |
| OLgf | varchar |  |  | SI | Log Level Filter 0 = log all 
1 = filter INSERT d... |
| OSCd | varchar |  |  | SI | Order/StockCode Generation  Mode(C,M,R),Prefix 
C... |
| Ocat | varchar |  |  | SI | Derived / Default Order Category
Format: Type,cod... |
| OpCl | varchar |  |  | SI | comma separated List e.g. 1,4 
0= no cleanup 
1=... |
| Osub | varchar |  |  | SI | Derived / Default Order Sub Category
Format: Type... |
| Pdro | varchar |  |  | SI | Prepend Generic to Order Desc 
and/or change Base... |
| Popa | varchar |  |  | SI | Purchase Order UOM 
Derive from Pack & Prefix, Ke... |
| Prc1 | varchar |  |  | SI | Copy Prc1 to Tariff 
Format: Y/N,Tariff Code,Curr... |
| Prc2 | varchar |  |  | SI | Copy Prc2 to Tariff 
Format: Y/N,Tariff Code,Curr... |
| Refr | varchar |  |  | SI | Cleanup 
0 = no cleanup / generate ONLY for Drugs... |
| RegConfGen | varchar |  |  | SI | - |
| RegPostGen | varchar |  |  | SI | - |
| RegPreGen | varchar |  |  | SI | Regional or Site Specific routines to be called
w... |
| Rloc | varchar |  |  | SI | Default Receiving Location for OrderCategory 
For... |
| Scat | varchar |  |  | SI | Stock Category 
Format: Code,Desc (for no Cat use... |
| Sloc | varchar |  |  | SI | Stock Main Location (code only) |
| Stbr | varchar |  |  | SI | Stock Batch Required Format: R/O/N (Required,Optio... |
| Sted | varchar |  |  | SI | Stock Expiry Date Required Format: R/O/N (Required... |
| Stgr | varchar |  |  | SI | Stock Take Group 
Format: Code,Desc (for no Group... |
| Stit | varchar |  |  | SI | Stock Issue/Transfer Format: I/T/B (Issue Only,Tra... |
| UPrA | varchar |  |  | SI | Update Pregnancy Alert  |
| UPrADMD | varchar |  |  | SI | Update Pregnancy Alert for generated DMD Level |
| UpdateDate | date |  |  | SI | Last Update Date |
| UpdateTime | time |  |  | SI | Last Update Time |
| UpdateUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*