# web_Msg.PA_AdmTransaction_TRANS_TempLocFreeText

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PA_AdmTransaction | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| TRANS_TempLocFreeText | varchar |  |  | SI | TRANS_TempLocFreeText |
| element_key | varchar |  |  | NO | TRANSTempLocFreeText array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*