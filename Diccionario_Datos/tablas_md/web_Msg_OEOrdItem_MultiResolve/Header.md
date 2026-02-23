# web_Msg_OEOrdItem_MultiResolve.Header

**Schema:** web_Msg_OEOrdItem_MultiResolve
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AdministrationRouteDR | bigint |  | FK | SI | - |
| AdmixAdditiveDR | varchar |  | FK | SI | - |
| BaseUOMDR | bigint |  | FK | SI | - |
| DispType | varchar |  |  | SI | - |
| DrugMasterDR | bigint |  | FK | SI | - |
| FormDR | bigint |  | FK | SI | - |
| Formulary | varchar |  |  | SI | - |
| GenericDR | bigint |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| IVType | varchar |  |  | SI | - |
| MultiDoseList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SomeDrugFormsHaveVolume | bit |  |  | SI | - |
| StockEnabled | varchar |  |  | SI | - |
| StockLocDR | bigint |  | FK | SI | - |
| StrengthDR | bigint |  | FK | SI | - |
| UOMDR | bigint |  | FK | SI | - |
| UseAdmixtureUOM | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*