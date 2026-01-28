# Admin Dashboard Access Guide

## Overview
The Admin Dashboard provides comprehensive analytics, disease prediction rates, model performance metrics, and system management capabilities for the Medical AI Prediction System.

## Access Requirements

### 1. Admin Email Configuration
To access the admin dashboard, your user account must be registered with one of the following admin emails:
- `admin@medai.com`
- `admin@example.com`

### 2. Registration Process
1. **Register with Admin Email**: Use one of the admin emails during registration
2. **Login**: Use your admin credentials to log in
3. **Automatic Redirect**: You'll be automatically redirected to the admin dashboard

## Features Available

### 📊 Disease Prediction Rates
- **Heart Disease Rate**: Percentage of positive heart disease predictions
- **Alzheimer Severe Rate**: Percentage of severe/moderate Alzheimer's predictions
- **Condition Detection**: Real-time condition detection from chat interactions

### 🎯 Model Performance Metrics
- **Accuracy Rates**: Individual model accuracy percentages
- **Error Rates**: Model error rates and misclassification analysis
- **Prediction Trends**: Recent prediction activity and performance trends
- **Overall Performance**: System-wide performance metrics

### 📈 Analytics Dashboard
- **User Statistics**: Total users, new users, active users
- **Chat Analytics**: Total chats, daily chat trends
- **Prediction Analytics**: Heart and Alzheimer prediction counts
- **Usage Trends**: 30-day usage patterns and growth metrics

### 👥 User Management
- **User Activity**: View all registered users and their activity
- **Chat History**: Monitor user interactions and AI responses
- **User Status**: Track active vs inactive users
- **User Details**: Individual user statistics and engagement

### 📋 Reporting System
- **Analytics Reports**: Complete system analytics and metrics
- **User Reports**: User activity and engagement data
- **Chat Reports**: All chat interactions and recommendations
- **Prediction Reports**: All AI predictions and results

## How to Access Admin Dashboard

### Method 1: Direct URL Access
1. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```

2. Start the frontend server:
   ```bash
   cd frontend
   npm run dev
   ```

3. Navigate to: `http://localhost:5173/admin-dashboard`

### Method 2: Through Login Flow
1. Go to: `http://localhost:5173/login`
2. Register with an admin email (`admin@medai.com` or `admin@example.com`)
3. Login with your credentials
4. You'll be automatically redirected to the admin dashboard

### Method 3: API Access
Access admin endpoints directly via API:
```bash
# Get admin dashboard data
curl -H "Authorization: Bearer YOUR_TOKEN" \
     http://localhost:8000/dashboard/admin

# Get user statistics
curl -H "Authorization: Bearer YOUR_TOKEN" \
     http://localhost:8000/dashboard/users
```

## Admin Dashboard Sections

### 1. Key Metrics Cards
- **Total Users**: System-wide user count
- **Total Chats**: All chat interactions
- **Heart Predictions**: Heart disease prediction count
- **Alzheimer Predictions**: Alzheimer's prediction count

### 2. Disease Prediction Rates
- Real-time disease prediction percentages
- Positive prediction counts
- Condition detection rates from chat analysis

### 3. Model Performance & Error Rates
- **Heart Model**: Accuracy, error rate, total predictions
- **Alzheimer Model**: Accuracy, error rate, total predictions
- **Overall Performance**: System-wide metrics

### 4. Daily Usage Trends
- Interactive charts showing usage patterns
- Chat activity trends
- Prediction activity trends
- User engagement metrics

### 5. Condition Analysis
- Pie charts showing condition distribution
- Most common conditions detected
- Chat-based condition analysis

### 6. User Activity Table
- Complete user list with activity status
- Chat counts per user
- Prediction counts per user
- Last active timestamps

### 7. Recent Chat Activity
- Latest chat interactions
- AI responses and recommendations
- Condition detection results
- Medicine recommendations

### 8. Download Reports
- **Analytics Report**: Complete system metrics
- **User Report**: User activity data
- **Chat Report**: All chat interactions
- **Predictions Report**: All AI predictions

## Enhanced Features

### 🫀 Heart Disease Chat Model
- Dedicated heart disease prediction chat
- Risk assessment and lifestyle recommendations
- Symptom analysis and emergency guidance
- Access via: `http://localhost:8000/heart-chat`

### 🧠 Alzheimer's Disease Model
- Enhanced hybrid model (XGBoost + CNN + RNN)
- Improved accuracy and error visualization
- Multi-class severity prediction

### 📊 Error Minimization Visualization
- Model comparison charts
- Confusion matrices
- Error analysis patterns
- Performance trend analysis

## Troubleshooting

### Common Issues

1. **Access Denied (403 Error)**
   - Ensure you're using an admin email
   - Check if your account is properly registered
   - Verify the email is in the admin list

2. **Dashboard Not Loading**
   - Check if backend server is running on port 8000
   - Verify frontend server is running on port 5173
   - Check browser console for errors

3. **No Data Showing**
   - Ensure database is connected
   - Check if there are users and predictions in the system
   - Verify admin permissions are working

4. **Model Performance Not Updating**
   - Run the enhanced model training script
   - Check if models are properly saved
   - Verify model evaluation is working

### Getting Help

1. **Check Logs**: Look at backend console for error messages
2. **Database Status**: Verify MongoDB connection
3. **Model Status**: Check if enhanced models are trained
4. **API Testing**: Test admin endpoints directly

## Security Notes

- Admin access is restricted to specific email addresses
- All admin endpoints require authentication
- User data is protected and anonymized in reports
- Regular security updates recommended

## Next Steps

1. **Train Enhanced Models**: Run the training script to get better accuracy
2. **Monitor Performance**: Use the dashboard to track model performance
3. **Generate Reports**: Download reports for analysis
4. **User Management**: Monitor user activity and engagement
5. **System Optimization**: Use metrics to improve the system

---

**Note**: This admin dashboard provides comprehensive insights into the Medical AI Prediction System. Regular monitoring and analysis of the metrics will help maintain optimal system performance and user satisfaction.
